import { RTMA } from "../msg_defs/test_defs.js";
import { RTMAClient } from "../../src/rtma.js";

let server = "127.0.0.1";
let port = 5678;
let module_id = 0;
let client = new RTMAClient(server, port, module_id);

let send_times = Array(250).fill(0.0);
let recv_times = Array(250).fill(0.0);

let dt = Array(250).fill(0.0);
let i = 0;
let tmp_max = -1;
let max_val = -1;
let prev_recv_time = null;
let prev_serial = null;

var stats = document.getElementById('stats');

client.on_connect = () => {
    client.subscribe([RTMA.MT.PING]);
}

client.on_message = (msg) => {
    if (msg.header.msg_type == RTMA.MT.PING) {
        if (prev_serial === null) {
            prev_serial = msg.data.serial_no;
        }
        else if (msg.data.serial_no != (prev_serial + 1)) {
            let drops = msg.data.serial_no - prev_serial;
            console.log(`Dropped ${drops} packets`);
        }

        prev_serial = msg.data.serial_no;
        send_times[i] = msg.header.send_time;
        recv_times[i] = msg.header.recv_time;

        if (prev_recv_time == null) {
            prev_recv_time = msg.header.recv_time;
            return;
        }
        else {
            dt[i] = msg.header.recv_time - prev_recv_time;
        }

        // dt[i] = msg.header.recv_time - msg.header.send_time;

        if (dt[i] > tmp_max) {
            tmp_max = dt[i];
        }

        if (dt[i] > max_val) {
            max_val = dt[i];
            // console.log(JSON.stringify(msg));
        }

        i = i + 1;
        prev_recv_time = msg.header.recv_time;

        if (i == 250) {
            i = 0;
            let sum = 0;
            let ssum = 0;
            dt.forEach(num => { sum += num; });
            let avg = sum / 250.0;
            dt.forEach(num => { ssum += Math.pow(num - avg, 2) })
            let std = Math.sqrt(ssum) / 250.0;
            let min_val = Math.min(...dt);
            stats.innerHTML = `${avg} +/- ${std} [${min_val} - ${tmp_max}] [worst: ${max_val}]`;
            tmp_max = -1;
        }
    }
};

client.connect();

