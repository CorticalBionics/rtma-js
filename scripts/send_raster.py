import pyrtma
import time
import random
import json
import numpy as np

import msg_defs.test_defs
from typing import List


class RasterTest:
    def __init__(self):
        self.mod = pyrtma.Client()
        self.mod.connect()
        self.mod.send_module_ready()
        self.seq_no = 0

    def get_random(self) -> List[int]:
        if random.random() > 0.8:
            return [random.randint(0, 1) for _ in range(32)]
        else:
            return [0 for _ in range(32)]

    def rand_snippet(self, n):
        record = dict(
            date="2000-01-01",
            subject="test",
            session_type="gui_test",
            session=1,
            set=2,
            block=3,
            trial=4,
            daq_channel=random.choice(list(range(12))),
            sync_sample=6,
            waveform_sample=7,
            pulse_start_sample=8,
            serial_no=n,
            array_channel=random.choice(list(range(64))),
            amp1=500,
            amp2=250,
            frequency=13,
            polarity=0,
            width1=200,
            width2=400,
            interphase=50,
            interphase_voltage=random.random(),
            error=None,
            waveform=np.random.rand(1, 100).tolist(),
        )

        return record

    def send_snippet(self, n):
        json.dumps(
            [self.rand_snippet(n) for _ in range(random.choice([1, 3, 5]))],
            separators=(",", ":"),
        ).encode()

    def send_status(self, data):
        """Send Voltage Monitor Status rtma messages."""
        status = msg_defs.test_defs.MDF_STATUS()
        status.msg = json.dumps(data).encode("ascii")
        status.msg_length = len(status.msg)
        self.mod.send_message(status)

    def run(self):
        msg = msg_defs.test_defs.MDF_RASTER()
        n = 0
        try:
            dt = 32 * 0.002
            while True:
                msg.seq_no = self.seq_no
                msg.bins[:] = list(
                    range(self.seq_no * 32 * 200, (self.seq_no + 1) * 32 * 200, 200)
                )
                msg.ai_0[:] = self.get_random()
                msg.ai_1[:] = self.get_random()
                msg.ai_2[:] = self.get_random()
                msg.ai_3[:] = self.get_random()
                msg.ai_4[:] = self.get_random()
                msg.ai_5[:] = self.get_random()
                msg.ai_6[:] = self.get_random()
                msg.ai_7[:] = self.get_random()
                msg.ai_8[:] = self.get_random()
                msg.ai_9[:] = self.get_random()
                msg.ai_10[:] = self.get_random()
                msg.ai_11[:] = self.get_random()

                self.mod.send_message(msg)

                # if random.random() > 0.5:
                #     self.send_snippet(n)

                now = time.perf_counter()
                while (time.perf_counter() - now) < dt:
                    pass

                if self.seq_no % 500 == 0:
                    n += 1
                    m = {}
                    m["type"] = random.choice(
                        [
                            "abnormal_notice",
                            "unexpected_pulse_notice",
                            "missing_pulse_notice",
                            "expired_input_notice",
                        ]
                    )
                    m["detail"] = f"This is status test {n}"
                    self.send_status(m)

                self.seq_no += 1
        except KeyboardInterrupt:
            pass
        finally:
            self.mod.disconnect()


if __name__ == "__main__":
    RasterTest().run()
