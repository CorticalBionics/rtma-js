import pyrtma
import sys

sys.path.append("../")

import msg_defs.test_defs2 as md

c = pyrtma.Client()
c.connect(server_name="127.0.0.1:7111")
msg = md.MDF_TRIAL_METADATA()
while True:
    c.send_message(msg)
    print(msg.to_json())
    msg.trial_num += 1
    input()
