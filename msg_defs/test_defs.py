import ctypes
import pyrtma

# Constants
MAX_MODULES = 200
DYN_MOD_ID_START = 100
MAX_HOSTS = 5
MAX_MESSAGE_TYPES = 10000
MIN_STREAM_TYPE = 9000
MAX_TIMERS = 100
MAX_INTERNAL_TIMERS = 20
MAX_RTMA_MSG_TYPE = 99
MAX_RTMA_MODULE_ID = 9
MAX_LOGGER_FILENAME_LENGTH = 256
MAX_CONTIGUOUS_MESSAGE_DATA = 9000
ALL_MESSAGE_TYPES = 2147483647

# String Constants

# Type Aliases
MODULE_ID = ctypes.c_short


HOST_ID = ctypes.c_short


MSG_TYPE = ctypes.c_int


MSG_COUNT = ctypes.c_int



# Host IDs
LOCAL_HOST = 0
ALL_HOSTS = 32767

# Module IDs
MID_MESSAGE_MANAGER = 0
MID_QUICK_LOGGER = 5

# Message Type IDs
MT_EXIT = 0
MT_KILL = 1
MT_ACKNOWLEDGE = 2
MT_CONNECT = 13
MT_DISCONNECT = 14
MT_SUBSCRIBE = 15
MT_UNSUBSCRIBE = 16
MT_PAUSE_SUBSCRIPTION = 85
MT_RESUME_SUBSCRIPTION = 86
MT_FAIL_SUBSCRIBE = 6
MT_FAILED_MESSAGE = 8
MT_FORCE_DISCONNECT = 82
MT_MODULE_READY = 26
MT_SAVE_MESSAGE_LOG = 56
MT_TIMING_MESSAGE = 80
MT_PING = 1000
MT_RASTER = 1001
MT_STATUS = 1002


# Struct Definitions
class RTMA_MSG_HEADER(ctypes.Structure):
    _fields_ = [
        ("msg_type", MSG_TYPE),
        ("msg_count", MSG_COUNT),
        ("send_time", ctypes.c_double),
        ("recv_time", ctypes.c_double),
        ("src_host_id", HOST_ID),
        ("src_mod_id", MODULE_ID),
        ("dest_host_id", HOST_ID),
        ("dest_mod_id", MODULE_ID),
        ("num_data_bytes", ctypes.c_int),
        ("remaining_bytes", ctypes.c_int),
        ("is_dynamic", ctypes.c_int),
        ("reserved", ctypes.c_int)
    ]


# Message Definitions
@pyrtma.message_def
class MDF_EXIT(pyrtma.MessageData):
    _fields_ = []
    type_id = 0
    type_name = "EXIT"
    type_hash = 0x095e0546
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_KILL(pyrtma.MessageData):
    _fields_ = []
    type_id = 1
    type_name = "KILL"
    type_hash = 0x82fc702d
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_ACKNOWLEDGE(pyrtma.MessageData):
    _fields_ = []
    type_id = 2
    type_name = "ACKNOWLEDGE"
    type_hash = 0xb725b581
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_CONNECT(pyrtma.MessageData):
    _fields_ = [
        ("logger_status", ctypes.c_short),
        ("daemon_status", ctypes.c_short)
    ]
    type_id = 13
    type_name = "CONNECT"
    type_hash = 0x6f2e3ca5
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_DISCONNECT(pyrtma.MessageData):
    _fields_ = []
    type_id = 14
    type_name = "DISCONNECT"
    type_hash = 0xd0126bf9
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_SUBSCRIBE(pyrtma.MessageData):
    _fields_ = [
        ("msg_type", MSG_TYPE)
    ]
    type_id = 15
    type_name = "SUBSCRIBE"
    type_hash = 0xf5b437c8
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_UNSUBSCRIBE(pyrtma.MessageData):
    _fields_ = [
        ("msg_type", MSG_TYPE)
    ]
    type_id = 16
    type_name = "UNSUBSCRIBE"
    type_hash = 0x193fb9e0
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_PAUSE_SUBSCRIPTION(pyrtma.MessageData):
    _fields_ = [
        ("msg_type", MSG_TYPE)
    ]
    type_id = 85
    type_name = "PAUSE_SUBSCRIPTION"
    type_hash = 0x22338a6d
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_RESUME_SUBSCRIPTION(pyrtma.MessageData):
    _fields_ = [
        ("msg_type", MSG_TYPE)
    ]
    type_id = 86
    type_name = "RESUME_SUBSCRIPTION"
    type_hash = 0xc56a97f2
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_FAIL_SUBSCRIBE(pyrtma.MessageData):
    _fields_ = [
        ("mod_id", MODULE_ID),
        ("reserved", ctypes.c_short),
        ("msg_type", MSG_TYPE)
    ]
    type_id = 6
    type_name = "FAIL_SUBSCRIBE"
    type_hash = 0x9ad70a15
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_FAILED_MESSAGE(pyrtma.MessageData):
    _fields_ = [
        ("dest_mod_id", MODULE_ID),
        ("reserved", ctypes.c_short * 3),
        ("time_of_failure", ctypes.c_double),
        ("msg_header", RTMA_MSG_HEADER)
    ]
    type_id = 8
    type_name = "FAILED_MESSAGE"
    type_hash = 0xdca545b2
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_FORCE_DISCONNECT(pyrtma.MessageData):
    _fields_ = [
        ("mod_id", ctypes.c_int)
    ]
    type_id = 82
    type_name = "FORCE_DISCONNECT"
    type_hash = 0xc37c54e8
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_MODULE_READY(pyrtma.MessageData):
    _fields_ = [
        ("mod_id", ctypes.c_int)
    ]
    type_id = 26
    type_name = "MODULE_READY"
    type_hash = 0xcc0a3aad
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_SAVE_MESSAGE_LOG(pyrtma.MessageData):
    _fields_ = [
        ("pathname", ctypes.c_char * 256),
        ("pathname_length", ctypes.c_int)
    ]
    type_id = 56
    type_name = "SAVE_MESSAGE_LOG"
    type_hash = 0x515569e9
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_TIMING_MESSAGE(pyrtma.MessageData):
    _fields_ = [
        ("timing", ctypes.c_ushort * 10000),
        ("ModulePID", ctypes.c_int * 200),
        ("send_time", ctypes.c_double)
    ]
    type_id = 80
    type_name = "TIMING_MESSAGE"
    type_hash = 0x3595c23e
    type_source = "D:\\GIT\\pyrtma\\src\\pyrtma\\core_defs\\core_defs.yaml"


@pyrtma.message_def
class MDF_PING(pyrtma.MessageData):
    _fields_ = [
        ("serial_no", ctypes.c_int)
    ]
    type_id = 1000
    type_name = "PING"
    type_hash = 0xe6f432ea
    type_source = "D:\\GIT\\rtma-js\\msg_defs\\test_defs.yaml"


@pyrtma.message_def
class MDF_RASTER(pyrtma.MessageData):
    _fields_ = [
        ("seq_no", ctypes.c_ulong),
        ("bins", ctypes.c_ulong * 32),
        ("ai_0", ctypes.c_ubyte * 32),
        ("ai_1", ctypes.c_ubyte * 32),
        ("ai_2", ctypes.c_ubyte * 32),
        ("ai_3", ctypes.c_ubyte * 32),
        ("ai_4", ctypes.c_ubyte * 32),
        ("ai_5", ctypes.c_ubyte * 32),
        ("ai_6", ctypes.c_ubyte * 32),
        ("ai_7", ctypes.c_ubyte * 32),
        ("ai_8", ctypes.c_ubyte * 32),
        ("ai_9", ctypes.c_ubyte * 32),
        ("ai_10", ctypes.c_ubyte * 32),
        ("ai_11", ctypes.c_ubyte * 32)
    ]
    type_id = 1001
    type_name = "RASTER"
    type_hash = 0xda51540c
    type_source = "D:\\GIT\\rtma-js\\msg_defs\\test_defs.yaml"


@pyrtma.message_def
class MDF_STATUS(pyrtma.MessageData):
    _fields_ = [
        ("msg_length", ctypes.c_int),
        ("msg", ctypes.c_char * 1024)
    ]
    type_id = 1002
    type_name = "STATUS"
    type_hash = 0x704571a8
    type_source = "D:\\GIT\\rtma-js\\msg_defs\\test_defs.yaml"


# Collect all info into one object
class _constants:
    MAX_MODULES = 200
    DYN_MOD_ID_START = 100
    MAX_HOSTS = 5
    MAX_MESSAGE_TYPES = 10000
    MIN_STREAM_TYPE = 9000
    MAX_TIMERS = 100
    MAX_INTERNAL_TIMERS = 20
    MAX_RTMA_MSG_TYPE = 99
    MAX_RTMA_MODULE_ID = 9
    MAX_LOGGER_FILENAME_LENGTH = 256
    MAX_CONTIGUOUS_MESSAGE_DATA = 9000
    ALL_MESSAGE_TYPES = 2147483647


class _HID:
    LOCAL_HOST = 0
    ALL_HOSTS = 32767


class _MID:
    MESSAGE_MANAGER = 0
    QUICK_LOGGER = 5


class _aliases:
    MODULE_ID = MODULE_ID
    HOST_ID = HOST_ID
    MSG_TYPE = MSG_TYPE
    MSG_COUNT = MSG_COUNT


class _SDF:
    RTMA_MSG_HEADER = RTMA_MSG_HEADER


class _MT:
    EXIT = 0
    KILL = 1
    ACKNOWLEDGE = 2
    CONNECT = 13
    DISCONNECT = 14
    SUBSCRIBE = 15
    UNSUBSCRIBE = 16
    PAUSE_SUBSCRIPTION = 85
    RESUME_SUBSCRIPTION = 86
    FAIL_SUBSCRIBE = 6
    FAILED_MESSAGE = 8
    FORCE_DISCONNECT = 82
    MODULE_READY = 26
    SAVE_MESSAGE_LOG = 56
    TIMING_MESSAGE = 80
    PING = 1000
    RASTER = 1001
    STATUS = 1002


class _MDF:
    EXIT = MDF_EXIT
    KILL = MDF_KILL
    ACKNOWLEDGE = MDF_ACKNOWLEDGE
    CONNECT = MDF_CONNECT
    DISCONNECT = MDF_DISCONNECT
    SUBSCRIBE = MDF_SUBSCRIBE
    UNSUBSCRIBE = MDF_UNSUBSCRIBE
    PAUSE_SUBSCRIPTION = MDF_PAUSE_SUBSCRIPTION
    RESUME_SUBSCRIPTION = MDF_RESUME_SUBSCRIPTION
    FAIL_SUBSCRIBE = MDF_FAIL_SUBSCRIBE
    FAILED_MESSAGE = MDF_FAILED_MESSAGE
    FORCE_DISCONNECT = MDF_FORCE_DISCONNECT
    MODULE_READY = MDF_MODULE_READY
    SAVE_MESSAGE_LOG = MDF_SAVE_MESSAGE_LOG
    TIMING_MESSAGE = MDF_TIMING_MESSAGE
    PING = MDF_PING
    RASTER = MDF_RASTER
    STATUS = MDF_STATUS


class _RTMA:
    constants = _constants
    HID = _HID
    MID = _MID
    aliases = _aliases
    MT = _MT
    MDF = _MDF
    SDF = _SDF


RTMA = _RTMA()