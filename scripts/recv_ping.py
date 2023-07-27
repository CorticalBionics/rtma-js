import pyrtma
import msg_defs.test_defs
import statistics

c = pyrtma.Client()
c.connect(server_name="127.0.0.1:7111")
msg = msg_defs.test_defs.MDF_PING()
stats = [0.0 for _ in range(250)]
i = 0
c.subscribe([msg_defs.test_defs.MT_PING])

tot_max = -1
while True:
    msg = c.read_message(timeout=0.100)
    if msg is None:
        continue
    if msg.type_id == msg_defs.test_defs.MT_PING:
        stats[i] = msg.header.recv_time - msg.header.send_time
        i += 1
        if i == 250:
            i = 0
            avg = statistics.mean(stats)
            std = statistics.mean(stats)
            if max(stats) > tot_max:
                tot_max = max(stats)

            print(
                f"{avg:06f} +/- {std:06f} [{min(stats):06f} - {max(stats):06f}] worst: {tot_max}"
            )
