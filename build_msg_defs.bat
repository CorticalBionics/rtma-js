@ECHO OFF
REM pyrtma msg_defs.py compiling
python -m pyrtma.compile -i ./msg_defs/mjvr_types.h .msg_defs/climber_config.h -o ./msg_defs/test_defs.js --js
python -m pyrtma.compile -i ./msg_defs/mjvr_types.h .msg_defs/climber_config.h -o ./msg_defs/test_defs.py --py