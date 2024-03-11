import pyrtma
import time
import sys

sys.path.append("../")
import msg_defs.test_defs
import statistics

c = pyrtma.Client()
c.connect(server_name="127.0.0.1:7111")
msg = msg_defs.test_defs.MDF_PING()
rate = 0.010
stats = [0.0 for _ in range(250)]
i = 0
serial = 0
while True:
    msg.serial_no += 1
    c.send_message(msg)
    t0 = time.perf_counter()
    while (time.perf_counter() - t0) < rate:
        pass

    stats[i] = t0
    i += 1
    if i == 250:
        i = 0
        diff = [a - b for a, b in zip(stats[1:], stats[:-1])]
        avg = statistics.mean(diff)
        std = statistics.stdev(diff)
        print(f"{avg:06f} +/- {std:06f} [{min(diff):06f} - {max(diff):06f}]")
