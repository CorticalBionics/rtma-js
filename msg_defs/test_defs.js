export { RTMA } ;

// Type Map Default Values
const type_map = {};
type_map.char = () => "";
type_map.unsigned_char = () => 0;
type_map.byte = () => 0;
type_map.int = () => 0;
type_map.signed_int = () => 0;
type_map.unsigned_int = () => 0;
type_map.unsigned = () => 0;
type_map.short = () => 0;
type_map.signed_short = () => 0;
type_map.unsigned_short = () => 0;
type_map.long = () => 0;
type_map.signed_long = () => 0;
type_map.unsigned_long = () => 0;
type_map.long_long = () => 0;
type_map.signed_long_long = () => 0;
type_map.unsigned_long_long = () => 0;
type_map.float = () => 0;
type_map.double = () => 0;
type_map.uint8 = () => 0;
type_map.uint16 = () => 0;
type_map.uint32 = () => 0;
type_map.uint64 = () => 0;
type_map.int8 = () => 0;
type_map.int16 = () => 0;
type_map.int32 = () => 0;
type_map.int64 = () => 0;

// Top-Level RTMA object
const RTMA = {};

// Constants
RTMA.constants =  {};
RTMA.constants.MAX_MODULES = 200;
RTMA.constants.DYN_MOD_ID_START = 100;
RTMA.constants.MAX_HOSTS = 5;
RTMA.constants.MAX_MESSAGE_TYPES = 10000;
RTMA.constants.MIN_STREAM_TYPE = 9000;
RTMA.constants.MAX_TIMERS = 100;
RTMA.constants.MAX_INTERNAL_TIMERS = 20;
RTMA.constants.MAX_RTMA_MSG_TYPE = 99;
RTMA.constants.MAX_RTMA_MODULE_ID = 9;
RTMA.constants.MAX_LOGGER_FILENAME_LENGTH = 256;
RTMA.constants.MAX_CONTIGUOUS_MESSAGE_DATA = 9000;
RTMA.constants.ALL_MESSAGE_TYPES = 2147483647;

// String Constants

// Type Aliases
RTMA.aliases =  {};

RTMA.aliases.MODULE_ID = type_map.short();
RTMA.aliases.HOST_ID = type_map.short();
RTMA.aliases.MSG_TYPE = type_map.int();
RTMA.aliases.MSG_COUNT = type_map.int();

// Host IDs
RTMA.HID =  {};

RTMA.HID.LOCAL_HOST = 0;
RTMA.HID.ALL_HOSTS = 32767;

// Module IDs
RTMA.MID =  {};

RTMA.MID.MESSAGE_MANAGER = 0;
RTMA.MID.QUICK_LOGGER = 5;

// Message Type IDs
RTMA.MT = {};

RTMA.MT.EXIT = 0;
RTMA.MT.KILL = 1;
RTMA.MT.ACKNOWLEDGE = 2;
RTMA.MT.CONNECT = 13;
RTMA.MT.DISCONNECT = 14;
RTMA.MT.SUBSCRIBE = 15;
RTMA.MT.UNSUBSCRIBE = 16;
RTMA.MT.PAUSE_SUBSCRIPTION = 85;
RTMA.MT.RESUME_SUBSCRIPTION = 86;
RTMA.MT.FAIL_SUBSCRIBE = 6;
RTMA.MT.FAILED_MESSAGE = 8;
RTMA.MT.FORCE_DISCONNECT = 82;
RTMA.MT.MODULE_READY = 26;
RTMA.MT.SAVE_MESSAGE_LOG = 56;
RTMA.MT.TIMING_MESSAGE = 80;
RTMA.MT.PING = 1000;

// Struct Definitions
RTMA.SDF = {};

RTMA.SDF.RTMA_MSG_HEADER = () => {
	return {
		msg_type: RTMA.aliases.MSG_TYPE(),
		msg_count: RTMA.aliases.MSG_COUNT(),
		send_time: type_map.double(),
		recv_time: type_map.double(),
		src_host_id: RTMA.aliases.HOST_ID(),
		src_mod_id: RTMA.aliases.MODULE_ID(),
		dest_host_id: RTMA.aliases.HOST_ID(),
		dest_mod_id: RTMA.aliases.MODULE_ID(),
		num_data_bytes: type_map.int(),
		remaining_bytes: type_map.int(),
		is_dynamic: type_map.int(),
		reserved: type_map.int()
	}
};

// Message Definitions
RTMA.MDF = {};

RTMA.MDF.EXIT = () => { return {} };

RTMA.MDF.KILL = () => { return {} };

RTMA.MDF.ACKNOWLEDGE = () => { return {} };

RTMA.MDF.CONNECT = () => {
	return {
		logger_status: type_map.short(),
		daemon_status: type_map.short()
	}
};

RTMA.MDF.DISCONNECT = () => { return {} };

RTMA.MDF.SUBSCRIBE = () => {
	return {
		msg_type: RTMA.aliases.MSG_TYPE()
	}
};

RTMA.MDF.UNSUBSCRIBE = () => {
	return {
		msg_type: RTMA.aliases.MSG_TYPE()
	}
};

RTMA.MDF.PAUSE_SUBSCRIPTION = () => {
	return {
		msg_type: RTMA.aliases.MSG_TYPE()
	}
};

RTMA.MDF.RESUME_SUBSCRIPTION = () => {
	return {
		msg_type: RTMA.aliases.MSG_TYPE()
	}
};

RTMA.MDF.FAIL_SUBSCRIBE = () => {
	return {
		mod_id: RTMA.aliases.MODULE_ID(),
		reserved: type_map.short(),
		msg_type: RTMA.aliases.MSG_TYPE()
	}
};

RTMA.MDF.FAILED_MESSAGE = () => {
	return {
		dest_mod_id: RTMA.aliases.MODULE_ID(),
		reserved: Array(3).fill(type_map.short()),
		time_of_failure: type_map.double(),
		msg_header: RTMA.SDF.RTMA_MSG_HEADER()
	}
};

RTMA.MDF.FORCE_DISCONNECT = () => {
	return {
		mod_id: type_map.int()
	}
};

RTMA.MDF.MODULE_READY = () => {
	return {
		mod_id: type_map.int()
	}
};

RTMA.MDF.SAVE_MESSAGE_LOG = () => {
	return {
		pathname: Array(256).fill(type_map.char()),
		pathname_length: type_map.int()
	}
};

RTMA.MDF.TIMING_MESSAGE = () => {
	return {
		timing: Array(10000).fill(type_map.unsigned_short()),
		ModulePID: Array(200).fill(type_map.int()),
		send_time: type_map.double()
	}
};

RTMA.MDF.PING = () => { return {} };

// Message Definition Hashes
RTMA.HASH = {};

RTMA.HASH.EXIT = "095e0546";
RTMA.HASH.KILL = "82fc702d";
RTMA.HASH.ACKNOWLEDGE = "b725b581";
RTMA.HASH.CONNECT = "6f2e3ca5";
RTMA.HASH.DISCONNECT = "d0126bf9";
RTMA.HASH.SUBSCRIBE = "f5b437c8";
RTMA.HASH.UNSUBSCRIBE = "193fb9e0";
RTMA.HASH.PAUSE_SUBSCRIPTION = "22338a6d";
RTMA.HASH.RESUME_SUBSCRIPTION = "c56a97f2";
RTMA.HASH.FAIL_SUBSCRIBE = "9ad70a15";
RTMA.HASH.FAILED_MESSAGE = "dca545b2";
RTMA.HASH.FORCE_DISCONNECT = "c37c54e8";
RTMA.HASH.MODULE_READY = "cc0a3aad";
RTMA.HASH.SAVE_MESSAGE_LOG = "515569e9";
RTMA.HASH.TIMING_MESSAGE = "3595c23e";
RTMA.HASH.PING = "4ebbbe74";
