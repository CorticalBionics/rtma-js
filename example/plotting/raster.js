import { RTMA } from "../../msg_defs/test_defs.js";
import { RTMAClient } from "../../src/rtma.js";

let replot = false;

let x = Array(1250).fill(0, 0);
for (let i = 0; i < 1250; i++) {
    x[i] = i * 0.002 - 2.5;
}


let data = [];
for (let i = 0; i < 12; i++) {
    data.push({
        x: x,
        y: Array(1250).fill(NaN, 0),
        mode: 'markers',
        type: 'scatter',
        name: `ai_${i}`,
        marker: { size: 3 }
    });


}

let layout = {
    title: 'Raster Plot',
    showlegend: false,
    xaxis: {
        title: "Time [s]",
    },
    yaxis: {
        title: "DAQ Channel",
        range: [0, 12],
        tickvals: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    }
};

let raster = document.getElementById('raster');
let log = document.getElementById('msg_log');

let button = document.createElement("button");
button.innerHTML = "UNSUBSCRIBE";
document.getElementById("btn").appendChild(button);

button.addEventListener("click", function () {
    if (button.innerHTML === "UNSUBSCRIBE") {
        client.unsubscribe([RTMA.MT.RASTER]);
        client.unsubscribe([RTMA.MT.STATUS]);
        button.innerHTML = "SUBSCRIBE";
    } else {
        client.subscribe([RTMA.MT.RASTER]);
        client.subscribe([RTMA.MT.STATUS]);
        button.innerHTML = "UNSUBSCRIBE";
    }
});

let notes = [];

Plotly.newPlot(raster, data, layout);
window.onresize = function () { Plotly.Plots.resize(raster); };

let server = "127.0.0.1";
let port = 5678;
let module_id = 0;
let client = new RTMAClient(server, port, module_id);

// Subscribe to the messages that we want
client.on_connect = function (event) {
    client.subscribe([RTMA.MT.RASTER]);
    client.subscribe([RTMA.MT.STATUS]);
}

let update = {};
client.on_message = function (msg) {
    if (msg.header.msg_type === RTMA.MT.RASTER) {
        update = { y: [] };
        // console.log(JSON.stringify(data));
        let i = 1;
        for (const trace of data) {
            trace.y = trace.y.slice(32, 1250).concat(msg.data[trace.name].map(x => x ? x * i : NaN));
            update.y.push(trace.y);
            i++;
        }
    }
    else if (msg.header.msg_type == RTMA.MT.STATUS) {
        let note = document.createElement("div");
        let status = JSON.parse(msg.data.msg)
        note.innerHTML = status.type;
        notes.unshift(note);
        if (notes.length > 10) {
            notes.pop();
        }
        log.replaceChildren(...notes);
    }

    replot = true;
};

client.connect();

const intervalID = setInterval(refresh, 100);

function refresh() {
    if (replot) {
        Plotly.restyle(raster, update);
        replot = false;
    }
}
