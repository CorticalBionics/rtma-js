import pyrtma
import msg_defs.test_defs
import time

c = pyrtma.Client(module_id=198)
c.connect(server_name="127.0.0.1:7111")

for mt, mdf in pyrtma.user_msg_defs.items():
    c.subscribe([mt])
    msg = c.wait_for_acknowledgement()
    if msg is None:
        raise RuntimeError
    c.send_message(mdf(), dest_mod_id=199)
    while True:
        msg = c.read_message(1)
        if msg and msg.data.type_id == mt:
            print(msg.header.pretty_print())
            print(msg.data.pretty_print())
            c.unsubscribe([mt])
            msg = c.wait_for_acknowledgement()
            if msg is None:
                raise RuntimeError
            break
        elif msg is not None:
            print(msg.data.type_name)
    input()
