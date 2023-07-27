import { RTMA } from "../../msg_defs/test_defs.js";
import { RTMAClient } from "../../src/rtma.js";

let server = "127.0.0.1";
let port = 5678;
let module_id = 0;
let client = new RTMAClient(server, port, module_id);
client.init();

let send_times = Array(250).fill(0.0);
let recv_times = Array(250).fill(0.0);
let dt = Array(250).fill(0.0);
// let tbw = Array(250).fill(0.0);
let i = 0;
let max_val = -1;
let prev_recv_time = -1;

client.on_connect = () => {
    client.subscribe(RTMA.MT.PING);
}

client.on_message = (msg) => {
    if (msg.header.msg_type == RTMA.MT.PING) {
        send_times[i] = msg.header.send_time;
        recv_times[i] = msg.header.recv_time;
        dt[i] = msg.header.recv_time - msg.header.send_time;
        if (prev_recv_time) {
            tbw[i] = msg.header.recv_time - prev_recv_time;
        }
        i = i + 1;
        prev_recv_time = msg.header.recv_time;

        if (i == 250) {
            i = 0;
            let sum = 0;
            let ssum = 0;
            dt.forEach(num => { sum += num; });
            // tbw.forEach(num => { sum += num; });
            let avg = sum / 250.0;
            dt.forEach(num => { ssum += Math.pow(num - avg, 2) })
            // tbw.forEach(num => { ssum += Math.pow(num - avg, 2) })
            let std = Math.sqrt(ssum) / 250.0;
            let min_val = Math.min(...dt);
            let tmp_max = Math.max(...dt);
            if (tmp_max > max_val) {
                max_val = tmp_max;
            }

            console.log(`${avg} +/- ${std} [${min_val} - ${tmp_max}] [worst: ${max_val}]`)
        }
    }
};


