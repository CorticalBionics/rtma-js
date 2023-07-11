import { RTMA } from "../../msg_defs/climber_config.js";
import { RTMAClient } from "../../src/rtma.js";

let server = "127.0.0.1";
let port = 5678;
let module_id = 0;
let client = new RTMAClient(server, port, module_id);
client.init();

client.on_connect = () => {
    client.subscribe(RTMA.MT.TRIAL_METADATA);
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
};


