import { RTMA } from "../../../climber_message/build/climber_message/message_defs.js";
import { RTMAClient } from "../../src/rtma.js";

let server = "127.0.0.1";
let port = 5678;
let module_id = 0;
let client = new RTMAClient(server, port, module_id);

// Install handlers before connecting
client.on_connect = () => {
    for (const [key, value] of Object.entries(RTMA.MT)) {
        if (value > 1200) {
            client.subscribe([RTMA.MT[key]]);
        };
    };
}

client.on_message = (msg) => {
    let name = "";
    for (const [key, value] of Object.entries(RTMA.MT)) {
        if (value == msg.header.msg_type) {
            name = `${key}`;
            break;
        }
    }


    console.log(`${name}: ${JSON.stringify(msg)}`);

    // Echo message back
    if (msg.header.msg_type > 1200)
        client.send_message(msg.header.msg_type, msg.data, msg.header.src_mod_id);

};

client.connect();


