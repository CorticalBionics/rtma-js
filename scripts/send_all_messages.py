import pyrtma
import sys
import climber_message

c = pyrtma.Client(module_id=198)
c.connect(server_name="127.0.0.1:7111")

for mt, mdf in pyrtma.msg_defs.items():
    if mt > 1200:
        c.subscribe([mt])
        msg = c.wait_for_acknowledgement()
        if msg is None:
            raise RuntimeError
        c.send_message(mdf.from_random())
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
