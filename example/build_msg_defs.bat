@ECHO OFF
REM pyrtma msg_defs.py compiling
python -m pyrtma.compile -i ./msg_defs/test_defs.yaml --js --py
python -m pyrtma.compile -i ./msg_defs/test_defs2.yaml --js --py