const CORE = {
  constants: {
    MAX_MODULES: 200,
    DYN_MOD_ID_START: 100,
    MAX_HOSTS: 5,
    MAX_MESSAGE_TYPES: 10000,
    MIN_STREAM_TYPE: 9000,
    MAX_TIMERS: 100,
    MAX_INTERNAL_TIMERS: 20,
    MAX_RTMA_MSG_TYPE: 99,
    MAX_RTMA_MODULE_ID: 9,
    MAX_LOGGER_FILENAME_LENGTH: 256,
    MAX_CONTIGUOUS_MESSAGE_DATA: 9000,
    HID_LOCAL_HOST: 0,
    HID_ALL_HOSTS: 0x7fff,
    ALL_MESSAGE_TYPES: 0x7fffffff,
  },

  MT: {
    EXIT: 0,
    KILL: 1,
    ACKNOWLEDGE: 2,
    CONNECT: 13,
    DISCONNECT: 14,
    SUBSCRIBE: 15,
    UNSUBSCRIBE: 16,
    PAUSE_SUBSCRIPTION: 85,
    FAIL_SUBSCRIBE: 6,
    FAILED_MESSAGE: 8,
    FORCED_DISCONNECT: 82,
    MODULE_READY: 26,
    SAVE_MESSAGE_LOG: 56,
    TIMING_MESSAGE: 80,
  },

  MID: {
    MESSAGE_MANAGER: 0,
    COMMAND_MODULE: 1,
    APPLICATION_MODULE: 2,
    NETWORK_RELAY: 3,
    STATUS_MODULE: 4,
    QUICKLOGGER: 5,
  },

  MDF: {
    RTMA_MSG_HEADER: () => {
      return {
        msg_type: 0,
        msg_count: 0,
        send_time: 0,
        recv_time: 0,
        src_host_id: 0,
        src_mod_id: 0,
        dest_host_id: 0,
        dest_mod_id: 0,
        num_data_bytes: 0,
        remaining_bytes: 0,
        is_dynamic: 0,
        reserved: 0,
      };
    },

    CONNECT: () => {
      return {
        logger_status: 0,
        daemon_status: 0,
      };
    },

    SUBSCRIBE: () => {
      return {
        msg_type: 0,
      };
    },

    UNSUBSCRIBE: () => {
      return {
        msg_type: 0,
      };
    },

    PAUSE_SUBSCRIPTION: () => {
      return {
        msg_type: 0,
      };
    },

    RESUME_SUBSCRIPTION: () => {
      return {
        msg_type: 0,
      };
    },

    FAIL_SUBSCRIBE: () => {
      return {
        mod_id: 0,
        reserved: 0,
        msg_type: 0,
      };
    },

    FAILED_MESSAGE: () => {
      return {
        dest_mod_id: 0,
        reserved: 0,
        time_of_failure: 0,
        msg_header: {
          msg_type: 0,
          msg_count: 0,
          send_time: 0,
          recv_time: 0,
          src_host_id: 0,
          src_mod_id: 0,
          dest_host_id: 0,
          dest_mod_id: 0,
          num_data_bytes: 0,
          remaining_bytes: 0,
          is_dynamic: 0,
          reserved: 0,
        },
      };
    },

    FORCE_DISCONNECT: () => {
      return {
        mod_id: 0,
      };
    },

    MODULE_READY: () => {
      return {
        mod_id: 0,
      };
    },

    SAVE_MESSAGE_LOG: () => {
      return {
        pathname: "",
        pathname_length: 0,
      };
    },

    TIMING_MESSAGE: () => {
      return {
        timing: Array(MAX_MESSAGE_TYPES).fill(0),
        ModulePID: Array(MAX_MODULES).fill(0),
        send_time: 0,
      };
    },

    EXIT: () => {
      return {};
    },

    KILL: () => {
      return {};
    },

    ACKNOWLEDGE: () => {
      return {};
    },

    DISCONNECT: () => {
      return {};
    },

    FORCED_DISCONNECT: () => {
      return {};
    },
  },
};

export class RTMAClient {
  constructor(server = "127.0.0.1", port = 5678, module_id = 0, host_id = 0) {
    this.server = server;
    this.port = port;
    this.ready = false;
    this.error = false;
    this.connected = false;
    this.host_id = host_id;
    this.module_id = module_id;
    this.msg_count = 0;
    this.pending_ack = false;
    this.ws = null;
    this.connect_ack = false;

    this.on_connect = () => {};

    this._on_connect = (msg) => {
      this.connected = true;
      // Store module id if dynamically assigned
      if (msg.header.dest_mod_id !== 0) {
        this.module_id = msg.header.dest_mod_id;
      }

      this.on_connect();
    };

    this.on_message = (msg) => {
      console.log(`${JSON.stringify(msg)}`);
    };
  }

  send_message(msg_type, msg_data, dest_mod_id = 0, dest_host_id = 0) {
    const hdr = CORE.MDF.RTMA_MSG_HEADER();
    hdr.msg_type = msg_type;
    hdr.msg_count = this.msg_count;
    hdr.recv_time = 0;
    hdr.send_time = Date.now() / 1000;
    hdr.src_host_id = this.host_id;
    hdr.src_mod_id = this.module_id;
    hdr.dest_host_id = dest_host_id;
    hdr.dest_mod_id = dest_mod_id;

    // The ws proxy will fill this data in after serializing
    hdr.num_data_bytes = 0;

    // Send through the websocket
    this.ws.send(JSON.stringify({ header: hdr, data: msg_data }));

    this.msg_count++;
  }

  send_signal(msg_type, dest_mod_id = 0, dest_host_id = 0) {
    const hdr = CORE.MDF.RTMA_MSG_HEADER();
    hdr.msg_type = msg_type;
    hdr.msg_count = this.msg_count;
    hdr.send_time = Date.now() / 1000;
    hdr.src_host_id = this.host_id;
    hdr.src_mod_id = this.module_id;
    hdr.dest_host_id = dest_host_id;
    hdr.dest_mod_id = dest_mod_id;
    hdr.num_data_bytes = 0;

    // Send through the websocket
    this.ws.send(JSON.stringify(hdr));

    this.msg_count++;
  }

  connect() {
    console.log("rtma.js connect");
    const msg = CORE.MDF.CONNECT();
    msg.logger_status = 0;
    msg.daemon_status = 0;
    this.send_message(CORE.MT.CONNECT, msg);
    this.connect_ack = true;
  }

  disconnect() {
    this.send_signal(CORE.MT.DISCONNECT);
    this.ready = false;
    this.connected = false;
    this.ws.close();
  }

  subscribe(msg_types) {
    msg_types.forEach((msg_type) => {
      const msg = CORE.MDF.SUBSCRIBE();
      msg.msg_type = msg_type;
      this.send_message(CORE.MT.SUBSCRIBE, msg);
    });
  }

  unsubscribe(msg_types) {
    msg_types.forEach((msg_type) => {
      const msg = CORE.MDF.UNSUBSCRIBE();
      msg.msg_type = msg_type;
      this.send_message(CORE.MT.UNSUBSCRIBE, msg);
    });
  }

  error_handler(msg) {
    console.log(msg.error);
    this.disconnect();
    this.connected = false;
    this.ready = false;
  }

  core_msg_handler(msg) {
    switch (msg.header.msg_type) {
      case CORE.MT.ACKNOWLEDGE:
        if (this.connect_ack) {
          this.connect_ack = false;
          this._on_connect(msg);
        }
        break;
      case CORE.MT.EXIT:
        break;
      default:
        break;
    }
  }

  init() {
    this.ws = new WebSocket(`ws://${this.server}:${this.port}`);
    const self = this;

    this.ws.onopen = function (event) {
      self.ready = true;
      self.connected = false;
      self.connect();
    };

    this.ws.onclose = function (event) {
      self.ready = false;
      self.connected = false;
      self.disconnect();
    };

    this.ws.onerror = function (event) {
      self.ready = false;
      self.error = event;
    };

    this.ws.onmessage = function (event) {
      // Get a timestamp
      const now = performance.now() / 1000.0; // seconds

      // Decode the rtma msg as json
      const msg = JSON.parse(event.data.replace(/Infinity/g, "1e1000"));

      // Handle error messages from the ws server
      if (msg.hasOwnProperty("error")) {
        error_handler(msg);
        return;
      }

      // Call the internal handler
      self.core_msg_handler(msg);

      // Over-write the proxy recv_time
      msg.header.recv_time = now;

      // Call the user installed message handler
      self.on_message(msg);
    };
  }
}
