import pyrtma
import sys
import msg_defs.climber_config

c = pyrtma.Client(module_id=198)
c.connect(server_name="127.0.0.1:7111")
msg = msg_defs.climber_config.MDF_TRIAL_METADATA()
while True:
    c.send_message(msg)
    print(msg.to_json())
    msg.trial_num += 1
    input()