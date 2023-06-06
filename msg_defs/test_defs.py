
import ctypes
import pyrtma
from pyrtma.constants import *

MJ_VR_MAX_MOCAP_COUNT = 32
MJ_VR_MAX_BODY_COUNT = 64
MJ_VR_MAX_MOTOR_COUNT = 32
MJ_VR_MAX_JOINT_COUNT = 64
MJ_VR_MAX_JOINT_DOF = 128
MJ_VR_MAX_CONTACT_COUNT = 32
MJ_VR_MAX_TENDON_COUNT = 32
MAX_SPIKE_SOURCES = 2
MAX_SPIKE_SOURCES_N256 = 1
MAX_SPIKE_CHANS_PER_SOURCE = 128
MAX_SPIKE_CHANS_PER_SOURCE_N256 = 256
MAX_COINCIDENT_SPIKES = 45
MAX_ANALOG_CHANS = 16
MAX_UNITS_PER_CHAN = 5
MAX_TOTAL_SPIKE_CHANS_PER_SOURCE = (MAX_SPIKE_CHANS_PER_SOURCE * MAX_UNITS_PER_CHAN)
MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256 = (MAX_SPIKE_CHANS_PER_SOURCE_N256 * MAX_UNITS_PER_CHAN)
MAX_TOTAL_SPIKE_CHANS = (MAX_SPIKE_SOURCES * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE)
MAX_TOTAL_SPIKE_CHANS_N256 = (MAX_SPIKE_SOURCES_N256 * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256)
LFPSAMPLES_PER_HEARTBEAT = 10
ANALOGSAMPLES_PER_HEARTBEAT = 10
RAW_COUNTS_PER_SAMPLE = 2
SAMPLE_LENGTH = (0.01 * RAW_COUNTS_PER_SAMPLE)
SNIPPETS_PER_MESSAGE = 25
SAMPLES_PER_SNIPPET = 48
MAX_DIG_PER_SAMPLE = 10
MAX_DATAGLOVE_SENSORS = 18
NUM_DOMAINS = 6
MAX_COMMAND_DIMS = 30
MPL_RAW_PERCEPT_DIMS = 54
NUM_STIM_CHANS = 64
SHAM_STIM_CHANS = 32
MAX_STIM_CHANS_ON = 12
PULSE_TRAIN_SIZE = 101
MAX_CS_CONFIGS = 16
NUM_SPIKES_PER_STIM_MSG = 26
MAX_XIPP_EEG_HEADSTAGES = 2
MAX_XIPP_CHANS = 32 * MAX_XIPP_EEG_HEADSTAGES
MAX_XIPP_ANALOG_CHANS = 32
XIPP_SAMPLES_PER_MSG = 20
MAX_MYO_EMG_CHANS = 8
MYO_SAMPLES_PER_MSG = 4
GRIP_DIMS_R = 1
GRIP_DIMS_L = 1
MAX_GRIP_DIMS = 9
MAX_GRIPPER_DIMS = 1
MAX_GRIPPER_JOINT_ANGLES = 5
MAX_GRIPPER_FORCES = 5
MJ_MAX_MOTOR = MAX_GRIPPER_DIMS
MJ_MAX_JOINT = MAX_GRIPPER_JOINT_ANGLES
MJ_MAX_CONTACT = MAX_GRIPPER_FORCES
NoResult = -1
SuccessfulTrial = 1
BadTrial = 2
ManualProceed = 4
ManualFail = 8
HX_DEKA_LUKE_CONTACT_COUNT = 13
HX_LUKE_MOTOR_COUNT = 6
NUM_FINGERS = 3
NUM_SENSORS_PER_FINGER = 9
NUM_SENSORS_PALM = 11
NUM_TAKKTILE = (NUM_FINGERS * NUM_SENSORS_PER_FINGER + NUM_SENSORS_PALM)
NUM_ENCODERS = NUM_FINGERS
NUM_SERVOS = 4
NUM_DYNAMIXEL = NUM_SERVOS
DEKA_DOF_COUNT = 7
KUKA_DOF_COUNT = 7
TAG_LENGTH = 64
MPL_AT_ARM_EPV_FING_JV = 0
MPL_AT_ARM_EPV_FING_JP = 1
MPL_AT_ARM_JV_FING_JP = 2
MPL_AT_ALL_JV = 3
MPL_AT_ALL_JP = 4
MPL_AT_ARM_EPP_FING_JP = 5
TFD_FREQ_BINS = 20
MUJOCO_LINK_ID = 1000
PRENSILIA_DOF = 5
PRENSILIA_EXT_SENSORS = 7

MT_MUJOCO_VR_REQUEST_STATE = 4213
MT_MUJOCO_VR_REPLY_STATE = 4214
MT_MUJOCO_VR_MOCAP_MOVE = 4215
MT_MUJOCO_VR_MOTOR_MOVE = 4216
MT_MUJOCO_VR_REQUEST_MODEL_INFO = 4217
MT_MUJOCO_VR_REPLY_MODEL_INFO = 4218
MT_MUJOCO_VR_REQUEST_LINK_STATE = 4219
MT_MUJOCO_VR_REPLY_LINK_STATE = 4220
MT_MUJOCO_VR_LINK = 4221
MT_MUJOCO_VR_LINK_RESET = 4222
MT_MUJOCO_VR_FLOATBODY_MOVE = 4223
MT_MUJOCO_VR_RESET = 4224
MT_MUJOCO_VR_RELOAD = 4225
MT_MUJOCO_VR_LOAD_MODEL = 4226
MT_MUJOCO_VR_PAUSE = 4227
MT_MUJOCO_VR_RESUME = 4228
MT_MUJOCO_VR_MOTOR_CTRL = 4229
MT_MUJOCO_VR_MOTOR_CONFIG = 4230
MT_MUJOCO_VR_SET_RGBA = 4231
MT_MUJOCO_VR_MSG = 4232
MT_FINISHED_COMMAND = 1700
MT_CONTROL_SPACE_FEEDBACK = 1701
MT_CONTROL_SPACE_COMMAND = 1702
MT_MPL_RAW_PERCEPT = 1703
MT_BIAS_COMMAND = 1704
MT_MPL_REBIASED_SENSORDATA = 1705
MT_CONTROL_SPACE_FEEDBACK_RHR_GRIPPER = 1706
MT_CONTROL_SPACE_POS_COMMAND = 1710
MT_MPL_SEGMENT_PERCEPTS = 1711
MT_WAM_FEEDBACK = 1712
MT_IMPEDANCE_COMMAND = 1713
MT_EXECUTIVE_CTRL = 1714
MT_CURSOR_FEEDBACK = 1720
MT_VISUAL_GRATING_BUILD = 1721
MT_VISUAL_GRATING_RESPONSE = 1722
MT_GRIP_COMMAND = 1730
MT_GRIP_FINISHED_COMMAND = 1731
MT_GRIPPER_FEEDBACK = 1732
MT_MUJOCO_SENSOR = 1733
MT_MUJOCO_CMD = 1734
MT_MUJOCO_MOVE = 1735
MT_MUJOCO_MSG = 1736
MT_MUJOCO_GHOST_COLOR = 1737
MT_MUJOCO_OBJMOVE = 1738
MT_OPENHAND_CMD = 1740
MT_OPENHAND_SENS = 1741
MT_PRENSILIA_SENS = 1742
MT_PRENSILIA_CMD = 1743
MT_TABLE_LOAD_CELLS = 1744
MT_REZERO_GRIPPER_SENSORS = 1745
MT_SINGLETACT_DATA = 1760
MT_RAW_SPIKECOUNT = 1800
MT_SPM_SPIKECOUNT = 1801
MT_SPIKE_SNIPPET = 1802
MT_RAW_CTSDATA = 1803
MT_SPM_CTSDATA = 1804
MT_REJECTED_SNIPPET = 1805
MT_RAW_DIGITAL_EVENT = 1806
MT_SPM_DIGITAL_EVENT = 1807
MT_STIM_SYNC_EVENT = 1808
MT_STIM_UPDATE_EVENT = 1809
MT_CENTRALRECORD = 1810
MT_RAW_ANALOGDATA = 1811
MT_SPM_ANALOGDATA = 1812
MT_RAW_SPIKECOUNT_N256 = 1815
MT_RAW_CTSDATA_N256 = 1816
MT_SAMPLE_GENERATED = 1820
MT_XIPP_EMG_DATA_RAW = 1830
MT_MYO_EMG_DATA = 1831
MT_MYO_KIN_DATA = 1832
MT_INPUT_DOF_DATA = 1850
MT_DATAGLOVE = 1860
MT_OPTITRACK_RIGID_BODY = 1861
MT_TASK_STATE_CONFIG = 1900
MT_PHASE_RESULT = 1901
MT_EXTRACTION_RESPONSE = 1902
MT_NORMALIZATION_FACTOR = 1903
MT_TRIAL_METADATA = 1904
MT_EXTRACTION_REQUEST = 1905
MT_UPDATE_UNIT_STATE = 1906
MT_DISABLED_UNITS = 1907
MT_TRIAL_END = 1910
MT_REP_START = 1911
MT_REP_END = 1912
MT_EXEC_SCORE = 1913
MT_FLIP_THAT_BUCKET_DATA = 1914
MT_EM_ADAPT_NOW = 2000
MT_EM_CONFIGURATION = 2001
MT_TDMS_CREATE = 2002
MT_RF_REPORT = 2003
MT_PICDISPLAY = 2004
MT_STIMDATA = 2005
MT_SEAIO_OUT = 2007
MT_ATIforcesensor = 2008
MT_TACTOR_CMD = 2009
MT_HSTLOG = 3000
MT_PLAYSOUND = 3100
MT_PLAYVIDEO = 3102
MT_START_TIMED_RECORDING = 3101
MT_AJA_CONFIG = 3200
MT_AJA_TIMECODE = 3201
MT_AJA_STATUS = 3202
MT_AJA_STATUS_REQUEST = 3203
MT_CERESTIM_CONFIG_MODULE = 4000
MT_CERESTIM_CONFIG_CHAN_PRESAFETY = 4001
MT_CERESTIM_CONFIG_CHAN = 4002
MT_CERESTIM_ERROR = 4003
MT_CERESTIM_ALIVE = 4004
MT_CS_TRAIN_END = 4005
MT_CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY = 4006
MT_CERESTIM_CONFIG_CHAN_ARBITRARY = 4007
MT_CS_ARBITRARY_CLOSE = 4008
MT_STIM_VOLTAGE_MONITOR_DATA = 4009
MT_STIM_VOLTAGE_MONITOR_DIGITAL_DATA = 4010
MT_VOLTAGE_MONITOR_STATUS = 4011
MT_STIM_DUTYCYCLE_TIME = 4012
MT_STIM_TRIAL_DURATION = 4013
MT_NATURAL_RESPONSE = 4050
MT_DEPTH_RESPONSE = 4051
MT_PAIN_RESPONSE = 4052
MT_MODALITY_TOGGLE = 4053
MT_MECH_RESPONSE = 4054
MT_MECH_INTENSITY_RESPONSE = 4055
MT_MOVE_RESPONSE = 4056
MT_MOVE_INTENSITY_RESPONSE = 4057
MT_TINGLE_RESPONSE = 4058
MT_TINGLE_INTENSITY_RESPONSE = 4059
MT_TEMP_RESPONSE = 4060
MT_DIR_PIXEL_COORDS = 4061
MT_PIXEL_COORDS = 4063
MT_CLEAR_LINE = 4064
MT_ADD_SENSATION = 4065
MT_SLIDER_DATA = 4066
MT_USER_DEFINED_STIM = 4067
MT_USER_BEHAVIOUR = 4068
MT_STOP_STIM = 4069
MT_PAUSE_TRIAL = 4070
MT_CST_LAMBDA = 4100
MT_CST_SETTINGS = 4101
MT_STIM_PRES_CONFIG = 4150
MT_STIM_PRES_PHASE_END = 4151
MT_STIM_PRESENT = 4152
MT_STIM_PRES_STATUS = 4153
MT_STIM_CONFIG_TYPE = 4154
MT_DEKA_ACI_RESPONSE = 4200
MT_DEKA_SENSOR = 4201
MT_DEKA_CAN_TOGGLE = 4202
MT_DEKA_CAN_GRIP_TOGGLE = 4203
MT_DEKA_CAN_EXIT = 4204
MT_DEKA_HAND_SENSOR = 4205
MT_DEKA_HAND_JSTICK_CMD = 4206
MT_RH_GRIPPER_SENSOR = 4207
MT_KUKA_JOINT_COMMAND = 4208
MT_KUKA_FEEDBACK = 4209
MT_KUKA_EXIT = 4210
MT_KUKA_PTP_JOINT = 4211
MT_KUKA_DEBUG = 4212
MT_TASKA_CMD = 4250
MT_TASKA_REPLY = 4251
MT_TASKA_ERROR = 4252
MT_MECH_STIM_CONFIGURE = 4240
MT_MECH_STIM_RESET = 4241
MT_MECH_STIM_STAGE = 4242
MT_MECH_STIM_WAITING = 4243
MT_MECH_STIM_TRIGGER = 4244
MT_MECH_STIM_CANCEL = 4245
MT_MECH_STIM_DONE = 4246
MT_MECH_STIM_ERROR = 4247

MID_MUJOCO_VR_MODULE = 61
MID_JSTICK_COMMAND = 10
MID_COMBINER = 11
MID_CEREBUS = 12
MID_INPUT_TRANSFORM = 20
MID_RPPL_RECORD = 21
MID_CENTRAL = 22
MID_EXTRACTION = 30
MID_MYO = 31
MID_MPL_CONTROL = 40
MID_GRIP_CONTROL = 41
MID_DEKA_CAN_MODULE = 42
MID_DEKA_ACI_RESPONSE = 43
MID_DEKA_DISPLAY = 44
MID_PSYCHTLBX = 46
MID_STIM_PRESENT = 48
MID_ACTIVE_ASSIST = 50
MID_KUKA_DISPLAY = 51
MID_ROBOTICS_FEEDBACK_INTEGRATOR = 52
MID_KUKA_INTERFACE_MODULE = 53
MID_KUKA_JOINT_COMMAND_DISPLAY = 54
MID_KUKA_DIAGNOSTICS = 55
MID_TASKA_DRIVER = 56
MID_FORCE_PLATFORM = 58
MID_FORCE_PLATFORM_DISPLAY = 59
MID_MPL_FEEDBACK = 60
MID_AJA_CONTROL = 65
MID_SEAIOCONTROL = 66
MID_EXECUTIVE = 70
MID_COMMENT_MANAGER = 71
MID_FLIP_THAT_BUCKET_MESSENGER = 74
MID_VOLTAGE_MONITOR_GUI = 76
MID_VOLTAGE_MONITOR = 77
MID_ATIsensor = 78
MID_MESSAGERATES = 81
MID_VISUAL_GRATING = 85
MID_BIASMODULE = 86
MID_CURSOR = 87
MID_RHR_COMMAND_MODULE = 88
MID_RHR_SENSOR_MODULE = 89
MID_SOUNDPLAYER = 90
MID_RFDISPLAY = 91
MID_RFACTIVITY = 92
MID_ImageDisplayer = 93
MID_FLIP_THAT_BUCKET = 94
MID_STIM_SAFETY_MODULE = 95
MID_SENSOR_STIM_TRANS_MODULE = 96
MID_CERESTIM_CONTROL = 97
MID_SENSE_TOUCH_INTERFACE = 98
MID_SENSOR_STIM_TRANSFORM_PY = 99
MID_MECH_STIM_MODULE = 0

SPIKE_COUNT_DATA_TYPE = ctypes.c_ubyte

class MJVR_MSG_HEADER(ctypes.Structure):
    _fields_ = [
        ("serial_no", ctypes.c_long),
        ("sub_sample", ctypes.c_long)
    ]


@pyrtma.msg_def
class MDF_MUJOCO_VR_REQUEST_STATE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER)
    ]
    type_id = MT_MUJOCO_VR_REQUEST_STATE
    type_name = "MUJOCO_VR_REQUEST_STATE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_REPLY_STATE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("requester_MID", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("sim_time", ctypes.c_double),
        ("body_position", ctypes.c_double * int(3 * MJ_VR_MAX_BODY_COUNT)),
        ("body_orientation", ctypes.c_double * int(4 * MJ_VR_MAX_BODY_COUNT)),
        ("motor_ctrltype", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("motor_position", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("motor_velocity", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("joint_position", ctypes.c_double * MJ_VR_MAX_JOINT_DOF),
        ("joint_velocity", ctypes.c_double * MJ_VR_MAX_JOINT_DOF),
        ("joint_torque", ctypes.c_double * MJ_VR_MAX_JOINT_DOF),
        ("contact", ctypes.c_double * MJ_VR_MAX_CONTACT_COUNT)
    ]
    type_id = MT_MUJOCO_VR_REPLY_STATE
    type_name = "MUJOCO_VR_REPLY_STATE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_REQUEST_MODEL_INFO(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER)
    ]
    type_id = MT_MUJOCO_VR_REQUEST_MODEL_INFO
    type_name = "MUJOCO_VR_REQUEST_MODEL_INFO"


@pyrtma.msg_def
class MDF_MUJOCO_VR_REPLY_MODEL_INFO(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("requester_MID", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("model_file", ctypes.c_char * 512),
        ("sim_time", ctypes.c_double),
        ("nq", ctypes.c_long),
        ("nv", ctypes.c_long),
        ("num_body", ctypes.c_long),
        ("num_mocap", ctypes.c_long),
        ("num_float", ctypes.c_long),
        ("num_motor", ctypes.c_long),
        ("num_joint", ctypes.c_long),
        ("num_contact", ctypes.c_long),
        ("num_tendon", ctypes.c_long),
        ("reserved1", ctypes.c_long),
        ("body_id", ctypes.c_long * MJ_VR_MAX_BODY_COUNT),
        ("mocap_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT),
        ("float_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT),
        ("motor_id", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("joint_id", ctypes.c_long * MJ_VR_MAX_JOINT_COUNT),
        ("contact_id", ctypes.c_long * MJ_VR_MAX_CONTACT_COUNT),
        ("tendon_id", ctypes.c_long * MJ_VR_MAX_TENDON_COUNT),
        ("joint_type", ctypes.c_long * MJ_VR_MAX_JOINT_COUNT),
        ("max_motor_limits", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("min_motor_limits", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("body_names", ctypes.c_char * 1024),
        ("mocap_names", ctypes.c_char * 1024),
        ("float_names", ctypes.c_char * 1024),
        ("motor_names", ctypes.c_char * 1024),
        ("joint_names", ctypes.c_char * 1024),
        ("contact_names", ctypes.c_char * 1024),
        ("tendon_names", ctypes.c_char * 1024)
    ]
    type_id = MT_MUJOCO_VR_REPLY_MODEL_INFO
    type_name = "MUJOCO_VR_REPLY_MODEL_INFO"


@pyrtma.msg_def
class MDF_MUJOCO_VR_REQUEST_LINK_STATE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER)
    ]
    type_id = MT_MUJOCO_VR_REQUEST_LINK_STATE
    type_name = "MUJOCO_VR_REQUEST_LINK_STATE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_REPLY_LINK_STATE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("requester_MID", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("nlink", ctypes.c_long),
        ("nfloat", ctypes.c_long),
        ("body_linkid", ctypes.c_long * MJ_VR_MAX_BODY_COUNT),
        ("link_followerid", ctypes.c_long * MJ_VR_MAX_BODY_COUNT),
        ("link_leaderid", ctypes.c_long * MJ_VR_MAX_BODY_COUNT),
        ("link_active", ctypes.c_char * MJ_VR_MAX_BODY_COUNT),
        ("link_rpos", ctypes.c_double * int(3 * MJ_VR_MAX_BODY_COUNT)),
        ("link_quat_leader", ctypes.c_double * int(4 * MJ_VR_MAX_BODY_COUNT)),
        ("link_quat_follower", ctypes.c_double * int(4 * MJ_VR_MAX_BODY_COUNT))
    ]
    type_id = MT_MUJOCO_VR_REPLY_LINK_STATE
    type_name = "MUJOCO_VR_REPLY_LINK_STATE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_LINK(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_links", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("follower_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT),
        ("leader_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT)
    ]
    type_id = MT_MUJOCO_VR_LINK
    type_name = "MUJOCO_VR_LINK"


@pyrtma.msg_def
class MDF_MUJOCO_VR_LINK_RESET(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_links", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("follower_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT)
    ]
    type_id = MT_MUJOCO_VR_LINK_RESET
    type_name = "MUJOCO_VR_LINK_RESET"


@pyrtma.msg_def
class MDF_MUJOCO_VR_MOCAP_MOVE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_id", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT),
        ("position", ctypes.c_double * int(3 * MJ_VR_MAX_MOCAP_COUNT)),
        ("orientation", ctypes.c_double * int(4 * MJ_VR_MAX_MOCAP_COUNT))
    ]
    type_id = MT_MUJOCO_VR_MOCAP_MOVE
    type_name = "MUJOCO_VR_MOCAP_MOVE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_MOTOR_MOVE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_id", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("id", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("position", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT)
    ]
    type_id = MT_MUJOCO_VR_MOTOR_MOVE
    type_name = "MUJOCO_VR_MOTOR_MOVE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_FLOATBODY_MOVE(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_id", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("float_body_id", ctypes.c_long * MJ_VR_MAX_MOCAP_COUNT),
        ("position", ctypes.c_double * int(3 * MJ_VR_MAX_MOCAP_COUNT)),
        ("orientation", ctypes.c_double * int(4 * MJ_VR_MAX_MOCAP_COUNT)),
        ("disable_link", ctypes.c_char * MJ_VR_MAX_MOCAP_COUNT)
    ]
    type_id = MT_MUJOCO_VR_FLOATBODY_MOVE
    type_name = "MUJOCO_VR_FLOATBODY_MOVE"


@pyrtma.msg_def
class MDF_MUJOCO_VR_LOAD_MODEL(pyrtma.MessageData):
    _fields_ = [
        ("model_filename", ctypes.c_char * 512)
    ]
    type_id = MT_MUJOCO_VR_LOAD_MODEL
    type_name = "MUJOCO_VR_LOAD_MODEL"


@pyrtma.msg_def
class MDF_MUJOCO_VR_SET_RGBA(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("type", ctypes.c_long),
        ("id", ctypes.c_long),
        ("rgba", ctypes.c_float * 4)
    ]
    type_id = MT_MUJOCO_VR_SET_RGBA
    type_name = "MUJOCO_VR_SET_RGBA"


@pyrtma.msg_def
class MDF_MUJOCO_VR_MOTOR_CONFIG(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_id", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("id", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("type", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("k_p", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("k_i", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("k_d", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("setpt", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT)
    ]
    type_id = MT_MUJOCO_VR_MOTOR_CONFIG
    type_name = "MUJOCO_VR_MOTOR_CONFIG"


@pyrtma.msg_def
class MDF_MUJOCO_VR_MOTOR_CTRL(pyrtma.MessageData):
    _fields_ = [
        ("header", MJVR_MSG_HEADER),
        ("num_id", ctypes.c_long),
        ("padding", ctypes.c_long),
        ("id", ctypes.c_long * MJ_VR_MAX_MOTOR_COUNT),
        ("ctrl", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT)
    ]
    type_id = MT_MUJOCO_VR_MOTOR_CTRL
    type_name = "MUJOCO_VR_MOTOR_CTRL"


@pyrtma.msg_def
class MDF_MUJOCO_VR_MSG(pyrtma.MessageData):
    _fields_ = [
        ("message", ctypes.c_char * 256),
        ("position", ctypes.c_long)
    ]
    type_id = MT_MUJOCO_VR_MSG
    type_name = "MUJOCO_VR_MSG"


class MSG_HEADER(ctypes.Structure):
    _fields_ = [
        ("serial_no", ctypes.c_long),
        ("sub_sample", ctypes.c_long)
    ]


@pyrtma.msg_def
class MDF_TRIAL_METADATA(pyrtma.MessageData):
    _fields_ = [
        ("session_num", ctypes.c_long),
        ("set_num", ctypes.c_long),
        ("block_num", ctypes.c_long),
        ("trial_num", ctypes.c_long),
        ("session_type", ctypes.c_char * 128),
        ("subject_id", ctypes.c_char * 64)
    ]
    type_id = MT_TRIAL_METADATA
    type_name = "TRIAL_METADATA"


@pyrtma.msg_def
class MDF_REP_START(pyrtma.MessageData):
    _fields_ = [
        ("rep_num", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_REP_START
    type_name = "REP_START"


@pyrtma.msg_def
class MDF_PLAYSOUND(pyrtma.MessageData):
    _fields_ = [
        ("filename", ctypes.c_char * 256)
    ]
    type_id = MT_PLAYSOUND
    type_name = "PLAYSOUND"


@pyrtma.msg_def
class MDF_PLAYVIDEO(pyrtma.MessageData):
    _fields_ = [
        ("filename", ctypes.c_char * 256)
    ]
    type_id = MT_PLAYVIDEO
    type_name = "PLAYVIDEO"


@pyrtma.msg_def
class MDF_START_TIMED_RECORDING(pyrtma.MessageData):
    _fields_ = [
        ("start_command", ctypes.c_double)
    ]
    type_id = MT_START_TIMED_RECORDING
    type_name = "START_TIMED_RECORDING"


@pyrtma.msg_def
class MDF_TASK_STATE_CONFIG(pyrtma.MessageData):
    _fields_ = [
        ("state_name", ctypes.c_char * 128),
        ("target", ctypes.c_double * MAX_COMMAND_DIMS),
        ("active_assist_weight", ctypes.c_double * NUM_DOMAINS),
        ("brain_control_weight", ctypes.c_double * NUM_DOMAINS),
        ("passive_assist_weight", ctypes.c_double * NUM_DOMAINS),
        ("jstick_control_weight", ctypes.c_double * NUM_DOMAINS),
        ("gain", ctypes.c_double * NUM_DOMAINS),
        ("threshold", ctypes.c_double * NUM_DOMAINS),
        ("force_targ", ctypes.c_double * MAX_GRIP_DIMS),
        ("dZ_gain", ctypes.c_double),
        ("force_thresh", ctypes.c_double),
        ("active_override", ctypes.c_long * MAX_COMMAND_DIMS),
        ("use_for_calib", ctypes.c_long),
        ("result_code", ctypes.c_long),
        ("stim_enable", ctypes.c_long),
        ("force_calib", ctypes.c_long),
        ("targ_set", ctypes.c_long),
        ("targ_idx", ctypes.c_long),
        ("gripperControlMask", ctypes.c_short * 4)
    ]
    type_id = MT_TASK_STATE_CONFIG
    type_name = "TASK_STATE_CONFIG"


@pyrtma.msg_def
class MDF_PHASE_RESULT(pyrtma.MessageData):
    _fields_ = [
        ("state_name", ctypes.c_char * 128),
        ("target", ctypes.c_double * MAX_COMMAND_DIMS),
        ("active_assist_weight", ctypes.c_double * NUM_DOMAINS),
        ("brain_control_weight", ctypes.c_double * NUM_DOMAINS),
        ("passive_assist_weight", ctypes.c_double * NUM_DOMAINS),
        ("jstick_control_weight", ctypes.c_double * NUM_DOMAINS),
        ("gain", ctypes.c_double * NUM_DOMAINS),
        ("threshold", ctypes.c_double * NUM_DOMAINS),
        ("force_targ", ctypes.c_double * MAX_GRIP_DIMS),
        ("dZ_gain", ctypes.c_double),
        ("force_thresh", ctypes.c_double),
        ("active_override", ctypes.c_long * MAX_COMMAND_DIMS),
        ("use_for_calib", ctypes.c_long),
        ("result_code", ctypes.c_long),
        ("stim_enable", ctypes.c_long),
        ("force_calib", ctypes.c_long),
        ("targ_set", ctypes.c_long),
        ("targ_idx", ctypes.c_long),
        ("gripperControlMask", ctypes.c_short * 4)
    ]
    type_id = MT_PHASE_RESULT
    type_name = "PHASE_RESULT"


@pyrtma.msg_def
class MDF_EXEC_SCORE(pyrtma.MessageData):
    _fields_ = [
        ("passed", ctypes.c_long),
        ("failed", ctypes.c_long)
    ]
    type_id = MT_EXEC_SCORE
    type_name = "EXEC_SCORE"


@pyrtma.msg_def
class MDF_FLIP_THAT_BUCKET_DATA(pyrtma.MessageData):
    _fields_ = [
        ("state_name", ctypes.c_char * 128),
        ("state_value", ctypes.c_double)
    ]
    type_id = MT_FLIP_THAT_BUCKET_DATA
    type_name = "FLIP_THAT_BUCKET_DATA"


@pyrtma.msg_def
class MDF_PICDISPLAY(pyrtma.MessageData):
    _fields_ = [
        ("filename", ctypes.c_char * 256),
        ("timer", ctypes.c_double)
    ]
    type_id = MT_PICDISPLAY
    type_name = "PICDISPLAY"


@pyrtma.msg_def
class MDF_STIMDATA(pyrtma.MessageData):
    _fields_ = [
        ("ConfigID", ctypes.c_double * 12),
        ("Vmax", ctypes.c_double * 12),
        ("Vmin", ctypes.c_double * 12),
        ("interphase", ctypes.c_double * 12)
    ]
    type_id = MT_STIMDATA
    type_name = "STIMDATA"


@pyrtma.msg_def
class MDF_TDMS_CREATE(pyrtma.MessageData):
    _fields_ = [
        ("pathname", ctypes.c_char * MAX_LOGGER_FILENAME_LENGTH),
        ("pathname_length", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_TDMS_CREATE
    type_name = "TDMS_CREATE"


@pyrtma.msg_def
class MDF_STIM_VOLTAGE_MONITOR_DATA(pyrtma.MessageData):
    _fields_ = [
        ("sample_rate", ctypes.c_long),
        ("pulse_count", ctypes.c_long),
        ("daq_channel", ctypes.c_long * NUM_SPIKES_PER_STIM_MSG),
        ("array_channel", ctypes.c_long * NUM_SPIKES_PER_STIM_MSG),
        ("daq_timestamp", ctypes.c_double * NUM_SPIKES_PER_STIM_MSG),
        ("voltage", ctypes.c_float * int(NUM_SPIKES_PER_STIM_MSG * 100)),
        ("interphase", ctypes.c_float * NUM_SPIKES_PER_STIM_MSG),
        ("Vmax", ctypes.c_float * NUM_SPIKES_PER_STIM_MSG),
        ("Vmin", ctypes.c_float * NUM_SPIKES_PER_STIM_MSG)
    ]
    type_id = MT_STIM_VOLTAGE_MONITOR_DATA
    type_name = "STIM_VOLTAGE_MONITOR_DATA"


@pyrtma.msg_def
class MDF_STIM_VOLTAGE_MONITOR_DIGITAL_DATA(pyrtma.MessageData):
    _fields_ = [
        ("stim_sync_event", ctypes.c_float * 30),
        ("stim_param_event", ctypes.c_float * 5),
        ("spm_daq_delta_t", ctypes.c_double)
    ]
    type_id = MT_STIM_VOLTAGE_MONITOR_DIGITAL_DATA
    type_name = "STIM_VOLTAGE_MONITOR_DIGITAL_DATA"


@pyrtma.msg_def
class MDF_VOLTAGE_MONITOR_STATUS(pyrtma.MessageData):
    _fields_ = [
        ("msg_length", ctypes.c_long),
        ("msg", ctypes.c_char * 1024)
    ]
    type_id = MT_VOLTAGE_MONITOR_STATUS
    type_name = "VOLTAGE_MONITOR_STATUS"


@pyrtma.msg_def
class MDF_STIM_DUTYCYCLE_TIME(pyrtma.MessageData):
    _fields_ = [
        ("dutycycle_time", ctypes.c_double)
    ]
    type_id = MT_STIM_DUTYCYCLE_TIME
    type_name = "STIM_DUTYCYCLE_TIME"


@pyrtma.msg_def
class MDF_STIM_TRIAL_DURATION(pyrtma.MessageData):
    _fields_ = [
        ("trial_duration", ctypes.c_double)
    ]
    type_id = MT_STIM_TRIAL_DURATION
    type_name = "STIM_TRIAL_DURATION"


@pyrtma.msg_def
class MDF_ATIforcesensor(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("Fx", ctypes.c_double),
        ("Fy", ctypes.c_double),
        ("Fz", ctypes.c_double),
        ("Tz", ctypes.c_double),
        ("Tx", ctypes.c_double),
        ("Ty", ctypes.c_double)
    ]
    type_id = MT_ATIforcesensor
    type_name = "ATIforcesensor"


@pyrtma.msg_def
class MDF_SEAIO_OUT(pyrtma.MessageData):
    _fields_ = [
        ("bit", ctypes.c_long),
        ("value", ctypes.c_long)
    ]
    type_id = MT_SEAIO_OUT
    type_name = "SEAIO_OUT"


@pyrtma.msg_def
class MDF_HSTLOG(pyrtma.MessageData):
    _fields_ = [
        ("len", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("log", ctypes.c_char * 512)
    ]
    type_id = MT_HSTLOG
    type_name = "HSTLOG"


@pyrtma.msg_def
class MDF_EM_CONFIGURATION(pyrtma.MessageData):
    _fields_ = [
        ("type", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("data", ctypes.c_char * 256)
    ]
    type_id = MT_EM_CONFIGURATION
    type_name = "EM_CONFIGURATION"


@pyrtma.msg_def
class MDF_EXTRACTION_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("src", ctypes.c_long),
        ("decoder_type", ctypes.c_char * 128),
        ("decoder_loc", ctypes.c_char * 256)
    ]
    type_id = MT_EXTRACTION_RESPONSE
    type_name = "EXTRACTION_RESPONSE"


@pyrtma.msg_def
class MDF_UPDATE_UNIT_STATE(pyrtma.MessageData):
    _fields_ = [
        ("unit_idx", ctypes.c_long),
        ("enabled", ctypes.c_long)
    ]
    type_id = MT_UPDATE_UNIT_STATE
    type_name = "UPDATE_UNIT_STATE"


@pyrtma.msg_def
class MDF_DISABLED_UNITS(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("disabled_units", ctypes.c_ubyte * MAX_TOTAL_SPIKE_CHANS)
    ]
    type_id = MT_DISABLED_UNITS
    type_name = "DISABLED_UNITS"


@pyrtma.msg_def
class MDF_CONTROL_SPACE_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("command", ctypes.c_double * MAX_COMMAND_DIMS),
        ("dZ", ctypes.c_double * MAX_GRIP_DIMS),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_CONTROL_SPACE_COMMAND
    type_name = "CONTROL_SPACE_COMMAND"


@pyrtma.msg_def
class MDF_BIAS_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("command", ctypes.c_double * MAX_COMMAND_DIMS),
        ("dZ", ctypes.c_double * MAX_GRIP_DIMS),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_BIAS_COMMAND
    type_name = "BIAS_COMMAND"


@pyrtma.msg_def
class MDF_IMPEDANCE_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stiffness", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_IMPEDANCE_COMMAND
    type_name = "IMPEDANCE_COMMAND"


@pyrtma.msg_def
class MDF_CONTROL_SPACE_POS_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("command", ctypes.c_double * MAX_COMMAND_DIMS),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_CONTROL_SPACE_POS_COMMAND
    type_name = "CONTROL_SPACE_POS_COMMAND"


@pyrtma.msg_def
class MDF_FINISHED_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("command", ctypes.c_double * MAX_COMMAND_DIMS),
        ("stiffness", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_FINISHED_COMMAND
    type_name = "FINISHED_COMMAND"


@pyrtma.msg_def
class MDF_EXECUTIVE_CTRL(pyrtma.MessageData):
    _fields_ = [
        ("proceed", ctypes.c_short),
        ("fail", ctypes.c_short),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_EXECUTIVE_CTRL
    type_name = "EXECUTIVE_CTRL"


@pyrtma.msg_def
class MDF_CONTROL_SPACE_FEEDBACK(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("position", ctypes.c_double * MAX_COMMAND_DIMS),
        ("velocity", ctypes.c_double * MAX_COMMAND_DIMS)
    ]
    type_id = MT_CONTROL_SPACE_FEEDBACK
    type_name = "CONTROL_SPACE_FEEDBACK"


@pyrtma.msg_def
class MDF_MPL_RAW_PERCEPT(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("position", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("velocity", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("torque", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("temperature", ctypes.c_double * MPL_RAW_PERCEPT_DIMS)
    ]
    type_id = MT_MPL_RAW_PERCEPT
    type_name = "MPL_RAW_PERCEPT"


@pyrtma.msg_def
class MDF_MPL_SEGMENT_PERCEPTS(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("ind_force", ctypes.c_double * 14),
        ("mid_force", ctypes.c_double * 14),
        ("rng_force", ctypes.c_double * 14),
        ("lit_force", ctypes.c_double * 14),
        ("thb_force", ctypes.c_double * 14),
        ("ind_accel", ctypes.c_double * 3),
        ("mid_accel", ctypes.c_double * 3),
        ("rng_accel", ctypes.c_double * 3),
        ("lit_accel", ctypes.c_double * 3),
        ("thb_accel", ctypes.c_double * 3),
        ("contacts", ctypes.c_short * 16)
    ]
    type_id = MT_MPL_SEGMENT_PERCEPTS
    type_name = "MPL_SEGMENT_PERCEPTS"


@pyrtma.msg_def
class MDF_MPL_REBIASED_SENSORDATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("torque", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("ind_force", ctypes.c_double * 14),
        ("mid_force", ctypes.c_double * 14),
        ("rng_force", ctypes.c_double * 14),
        ("lit_force", ctypes.c_double * 14),
        ("thb_force", ctypes.c_double * 14),
        ("contacts", ctypes.c_short * 16)
    ]
    type_id = MT_MPL_REBIASED_SENSORDATA
    type_name = "MPL_REBIASED_SENSORDATA"


@pyrtma.msg_def
class MDF_CURSOR_FEEDBACK(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("torque", ctypes.c_double * MPL_RAW_PERCEPT_DIMS),
        ("ind_force", ctypes.c_double * 14),
        ("mid_force", ctypes.c_double * 14),
        ("rng_force", ctypes.c_double * 14),
        ("lit_force", ctypes.c_double * 14),
        ("thb_force", ctypes.c_double * 14),
        ("contacts", ctypes.c_short * 16)
    ]
    type_id = MT_CURSOR_FEEDBACK
    type_name = "CURSOR_FEEDBACK"


@pyrtma.msg_def
class MDF_VISUAL_GRATING_BUILD(pyrtma.MessageData):
    _fields_ = [
        ("grating_visibility", ctypes.c_short),
        ("stimulation_on", ctypes.c_short),
        ("trial_set", ctypes.c_short),
        ("presentation", ctypes.c_short),
        ("increment_block", ctypes.c_short),
        ("wait_response", ctypes.c_short),
        ("reserved", ctypes.c_short)
    ]
    type_id = MT_VISUAL_GRATING_BUILD
    type_name = "VISUAL_GRATING_BUILD"


@pyrtma.msg_def
class MDF_VISUAL_GRATING_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("channel", ctypes.c_short),
        ("session_num", ctypes.c_short),
        ("set_num", ctypes.c_short),
        ("block_num", ctypes.c_short),
        ("trial_num", ctypes.c_short),
        ("block_ID", ctypes.c_short),
        ("DELTA_reference_frequency", ctypes.c_short),
        ("ICMS_reference_frequency", ctypes.c_float),
        ("ICMS_reference_amplitude", ctypes.c_float),
        ("ICMS_frequency_1", ctypes.c_float),
        ("ICMS_frequency_2", ctypes.c_float),
        ("ICMS_amplitude_1", ctypes.c_float),
        ("ICMS_amplitude_2", ctypes.c_float),
        ("VIS_reference_frequency", ctypes.c_float),
        ("VIS_reference_amplitude", ctypes.c_float),
        ("VIS_frequency_1", ctypes.c_float),
        ("VIS_frequency_2", ctypes.c_float),
        ("VIS_amplitude_1", ctypes.c_float),
        ("VIS_amplitude_2", ctypes.c_float),
        ("response", ctypes.c_short)
    ]
    type_id = MT_VISUAL_GRATING_RESPONSE
    type_name = "VISUAL_GRATING_RESPONSE"


@pyrtma.msg_def
class MDF_WAM_FEEDBACK(pyrtma.MessageData):
    _fields_ = [
        ("position", ctypes.c_double * 7),
        ("velocity", ctypes.c_double * 7)
    ]
    type_id = MT_WAM_FEEDBACK
    type_name = "WAM_FEEDBACK"


@pyrtma.msg_def
class MDF_RAW_CTSDATA(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("num_chans_enabled", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_short * int(LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_CHANS_PER_SOURCE))
    ]
    type_id = MT_RAW_CTSDATA
    type_name = "RAW_CTSDATA"


@pyrtma.msg_def
class MDF_RAW_CTSDATA_N256(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("num_chans_enabled", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_short * int(LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_CHANS_PER_SOURCE_N256))
    ]
    type_id = MT_RAW_CTSDATA_N256
    type_name = "RAW_CTSDATA_N256"


@pyrtma.msg_def
class MDF_RAW_ANALOGDATA(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("num_chans_enabled", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_short * int(ANALOGSAMPLES_PER_HEARTBEAT * MAX_ANALOG_CHANS))
    ]
    type_id = MT_RAW_ANALOGDATA
    type_name = "RAW_ANALOGDATA"


@pyrtma.msg_def
class MDF_SPM_CTSDATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_double * MAX_SPIKE_SOURCES),
        ("data", ctypes.c_short * int(RAW_COUNTS_PER_SAMPLE * LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_SOURCES * MAX_SPIKE_CHANS_PER_SOURCE))
    ]
    type_id = MT_SPM_CTSDATA
    type_name = "SPM_CTSDATA"


@pyrtma.msg_def
class MDF_SPM_ANALOGDATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_double * MAX_SPIKE_SOURCES),
        ("data", ctypes.c_short * int(RAW_COUNTS_PER_SAMPLE * LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_SOURCES * MAX_ANALOG_CHANS))
    ]
    type_id = MT_SPM_ANALOGDATA
    type_name = "SPM_ANALOGDATA"


@pyrtma.msg_def
class MDF_RAW_SPIKECOUNT(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("count_interval", ctypes.c_double),
        ("counts", ctypes.c_ubyte * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE)
    ]
    type_id = MT_RAW_SPIKECOUNT
    type_name = "RAW_SPIKECOUNT"


@pyrtma.msg_def
class MDF_RAW_SPIKECOUNT_N256(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("count_interval", ctypes.c_double),
        ("counts", ctypes.c_ubyte * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256)
    ]
    type_id = MT_RAW_SPIKECOUNT_N256
    type_name = "RAW_SPIKECOUNT_N256"


@pyrtma.msg_def
class MDF_SPM_SPIKECOUNT(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_double * MAX_SPIKE_SOURCES),
        ("count_interval", ctypes.c_double),
        ("counts", SPIKE_COUNT_DATA_TYPE * MAX_TOTAL_SPIKE_CHANS)
    ]
    type_id = MT_SPM_SPIKECOUNT
    type_name = "SPM_SPIKECOUNT"


class SPIKE_SNIPPET(ctypes.Structure):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("channel", ctypes.c_short),
        ("unit", ctypes.c_ubyte),
        ("reserved1", ctypes.c_ubyte),
        ("source_timestamp", ctypes.c_double),
        ("fPattern", ctypes.c_double * 3),
        ("nPeak", ctypes.c_short),
        ("nValley", ctypes.c_short),
        ("reserved2", ctypes.c_long),
        ("snippet", ctypes.c_short * SAMPLES_PER_SNIPPET)
    ]


@pyrtma.msg_def
class MDF_SPIKE_SNIPPET(pyrtma.MessageData):
    _fields_ = [
        ("ss", SPIKE_SNIPPET * SNIPPETS_PER_MESSAGE)
    ]
    type_id = MT_SPIKE_SNIPPET
    type_name = "SPIKE_SNIPPET"


class REJECTED_SNIPPET(ctypes.Structure):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("channel", ctypes.c_short),
        ("unit", ctypes.c_ubyte),
        ("reserved1", ctypes.c_ubyte),
        ("source_timestamp", ctypes.c_double),
        ("fPattern", ctypes.c_double * 3),
        ("nPeak", ctypes.c_short),
        ("nValley", ctypes.c_short),
        ("rejectType", ctypes.c_long),
        ("snippet", ctypes.c_short * SAMPLES_PER_SNIPPET)
    ]


@pyrtma.msg_def
class MDF_REJECTED_SNIPPET(pyrtma.MessageData):
    _fields_ = [
        ("rs", REJECTED_SNIPPET * SNIPPETS_PER_MESSAGE)
    ]
    type_id = MT_REJECTED_SNIPPET
    type_name = "REJECTED_SNIPPET"


@pyrtma.msg_def
class MDF_RAW_DIGITAL_EVENT(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("channel", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_ulong * 2)
    ]
    type_id = MT_RAW_DIGITAL_EVENT
    type_name = "RAW_DIGITAL_EVENT"


@pyrtma.msg_def
class MDF_SPM_DIGITAL_EVENT(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_index", ctypes.c_long * MAX_DIG_PER_SAMPLE),
        ("source_timestamp", ctypes.c_double * MAX_SPIKE_SOURCES),
        ("byte0", ctypes.c_ushort * MAX_DIG_PER_SAMPLE),
        ("byte1", ctypes.c_ushort * MAX_DIG_PER_SAMPLE),
        ("num_events", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_SPM_DIGITAL_EVENT
    type_name = "SPM_DIGITAL_EVENT"


@pyrtma.msg_def
class MDF_STIM_SYNC_EVENT(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("channel", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_ulong),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_STIM_SYNC_EVENT
    type_name = "STIM_SYNC_EVENT"


@pyrtma.msg_def
class MDF_STIM_UPDATE_EVENT(pyrtma.MessageData):
    _fields_ = [
        ("source_index", ctypes.c_long),
        ("channel", ctypes.c_long),
        ("source_timestamp", ctypes.c_double),
        ("data", ctypes.c_ulong),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_STIM_UPDATE_EVENT
    type_name = "STIM_UPDATE_EVENT"


@pyrtma.msg_def
class MDF_CENTRALRECORD(pyrtma.MessageData):
    _fields_ = [
        ("pathname", ctypes.c_char * MAX_LOGGER_FILENAME_LENGTH),
        ("subjectID", ctypes.c_char * int(MAX_LOGGER_FILENAME_LENGTH / 2)),
        ("record", ctypes.c_ulong),
        ("reserved", ctypes.c_ulong)
    ]
    type_id = MT_CENTRALRECORD
    type_name = "CENTRALRECORD"


@pyrtma.msg_def
class MDF_INPUT_DOF_DATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("tag", ctypes.c_char * TAG_LENGTH),
        ("dof_vals", ctypes.c_double * MAX_COMMAND_DIMS)
    ]
    type_id = MT_INPUT_DOF_DATA
    type_name = "INPUT_DOF_DATA"


@pyrtma.msg_def
class MDF_DATAGLOVE(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("tag", ctypes.c_char * TAG_LENGTH),
        ("raw_vals", ctypes.c_double * MAX_DATAGLOVE_SENSORS),
        ("calib_vals", ctypes.c_double * MAX_DATAGLOVE_SENSORS),
        ("gesture", ctypes.c_long),
        ("glovetype", ctypes.c_long),
        ("hand", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_DATAGLOVE
    type_name = "DATAGLOVE"


@pyrtma.msg_def
class MDF_SLIDER_DATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("type", ctypes.c_long),
        ("channel", ctypes.c_long),
        ("value", ctypes.c_long),
        ("time", ctypes.c_long)
    ]
    type_id = MT_SLIDER_DATA
    type_name = "SLIDER_DATA"


@pyrtma.msg_def
class MDF_USER_DEFINED_STIM(pyrtma.MessageData):
    _fields_ = [
        ("frequency", ctypes.c_long),
        ("amplitude", ctypes.c_long * 3),
        ("channel", ctypes.c_long * 3)
    ]
    type_id = MT_USER_DEFINED_STIM
    type_name = "USER_DEFINED_STIM"


@pyrtma.msg_def
class MDF_USER_BEHAVIOUR(pyrtma.MessageData):
    _fields_ = [
        ("current_trial", ctypes.c_long),
        ("current_screen", ctypes.c_char * 256),
        ("current_object", ctypes.c_char * 256),
        ("left_canvas", ctypes.c_long * 2),
        ("right_canvas", ctypes.c_long * 2),
        ("frequency", ctypes.c_long),
        ("freq_choice", ctypes.c_long),
        ("bio", ctypes.c_long),
        ("drag", ctypes.c_long),
        ("amplitude", ctypes.c_long * 3),
        ("satisfaction", ctypes.c_long),
        ("certainty", ctypes.c_long),
        ("chosen_object", ctypes.c_char * 256),
        ("object_quest", ctypes.c_long * 6),
        ("affective_quest", ctypes.c_long * 5)
    ]
    type_id = MT_USER_BEHAVIOUR
    type_name = "USER_BEHAVIOUR"


@pyrtma.msg_def
class MDF_STOP_STIM(pyrtma.MessageData):
    _fields_ = [
        ("stop_stim", ctypes.c_long)
    ]
    type_id = MT_STOP_STIM
    type_name = "STOP_STIM"


@pyrtma.msg_def
class MDF_PAUSE_TRIAL(pyrtma.MessageData):
    _fields_ = [
        ("pause_trial", ctypes.c_long)
    ]
    type_id = MT_PAUSE_TRIAL
    type_name = "PAUSE_TRIAL"


@pyrtma.msg_def
class MDF_CERESTIM_CONFIG_MODULE(pyrtma.MessageData):
    _fields_ = [
        ("configID", ctypes.c_long * MAX_CS_CONFIGS),
        ("amp1", ctypes.c_long * MAX_CS_CONFIGS),
        ("amp2", ctypes.c_long * MAX_CS_CONFIGS),
        ("frequency", ctypes.c_long * MAX_CS_CONFIGS),
        ("num_modules", ctypes.c_long),
        ("afcf", ctypes.c_long),
        ("width1", ctypes.c_long),
        ("width2", ctypes.c_long),
        ("interphase", ctypes.c_long)
    ]
    type_id = MT_CERESTIM_CONFIG_MODULE
    type_name = "CERESTIM_CONFIG_MODULE"


@pyrtma.msg_def
class MDF_CERESTIM_CONFIG_CHAN(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stop", ctypes.c_long),
        ("numChans", ctypes.c_long),
        ("channel", ctypes.c_long * MAX_STIM_CHANS_ON),
        ("pattern", ctypes.c_long * MAX_STIM_CHANS_ON),
        ("reps", ctypes.c_long),
        ("pause_t", ctypes.c_float)
    ]
    type_id = MT_CERESTIM_CONFIG_CHAN
    type_name = "CERESTIM_CONFIG_CHAN"


@pyrtma.msg_def
class MDF_CERESTIM_CONFIG_CHAN_ARBITRARY(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stop", ctypes.c_long),
        ("pathname", ctypes.c_char * MAX_LOGGER_FILENAME_LENGTH),
        ("pathlength", ctypes.c_long),
        ("pulselength", ctypes.c_long)
    ]
    type_id = MT_CERESTIM_CONFIG_CHAN_ARBITRARY
    type_name = "CERESTIM_CONFIG_CHAN_ARBITRARY"


@pyrtma.msg_def
class MDF_CERESTIM_CONFIG_CHAN_PRESAFETY(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stop", ctypes.c_long),
        ("numChans", ctypes.c_long),
        ("channel", ctypes.c_long * NUM_STIM_CHANS),
        ("pattern", ctypes.c_long * NUM_STIM_CHANS),
        ("reps", ctypes.c_long),
        ("pause_t", ctypes.c_float)
    ]
    type_id = MT_CERESTIM_CONFIG_CHAN_PRESAFETY
    type_name = "CERESTIM_CONFIG_CHAN_PRESAFETY"


@pyrtma.msg_def
class MDF_CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stop", ctypes.c_long),
        ("numChans", ctypes.c_long),
        ("channel", ctypes.c_long * NUM_STIM_CHANS),
        ("pattern", ctypes.c_long * NUM_STIM_CHANS),
        ("reps", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("pathname", ctypes.c_char * MAX_LOGGER_FILENAME_LENGTH),
        ("pathlength", ctypes.c_long)
    ]
    type_id = MT_CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY
    type_name = "CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY"


@pyrtma.msg_def
class MDF_CERESTIM_ERROR(pyrtma.MessageData):
    _fields_ = [
        ("error", ctypes.c_long),
        ("config", ctypes.c_long)
    ]
    type_id = MT_CERESTIM_ERROR
    type_name = "CERESTIM_ERROR"


@pyrtma.msg_def
class MDF_RF_REPORT(pyrtma.MessageData):
    _fields_ = [
        ("handp", ctypes.c_char * 48),
        ("handd", ctypes.c_char * 18),
        ("head", ctypes.c_char * 13),
        ("arms", ctypes.c_char * 20),
        ("tag", ctypes.c_long),
        ("flipframe", ctypes.c_long)
    ]
    type_id = MT_RF_REPORT
    type_name = "RF_REPORT"


@pyrtma.msg_def
class MDF_AJA_CONFIG(pyrtma.MessageData):
    _fields_ = [
        ("record", ctypes.c_long),
        ("stop", ctypes.c_long),
        ("filename", ctypes.c_char * 256)
    ]
    type_id = MT_AJA_CONFIG
    type_name = "AJA_CONFIG"


@pyrtma.msg_def
class MDF_AJA_TIMECODE(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("timecode", ctypes.c_char * 128)
    ]
    type_id = MT_AJA_TIMECODE
    type_name = "AJA_TIMECODE"


@pyrtma.msg_def
class MDF_AJA_STATUS(pyrtma.MessageData):
    _fields_ = [
        ("status", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("clipname", ctypes.c_char * 256)
    ]
    type_id = MT_AJA_STATUS
    type_name = "AJA_STATUS"


@pyrtma.msg_def
class MDF_NORMALIZATION_FACTOR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("factor", ctypes.c_double),
        ("length", ctypes.c_double)
    ]
    type_id = MT_NORMALIZATION_FACTOR
    type_name = "NORMALIZATION_FACTOR"


@pyrtma.msg_def
class MDF_CST_LAMBDA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("lambda", ctypes.c_float),
        ("k", ctypes.c_long),
        ("cursor_pos", ctypes.c_double)
    ]
    type_id = MT_CST_LAMBDA
    type_name = "CST_LAMBDA"


@pyrtma.msg_def
class MDF_CST_SETTINGS(pyrtma.MessageData):
    _fields_ = [
        ("sweep_rate", ctypes.c_double),
        ("vis_bins", ctypes.c_long),
        ("stim_bins", ctypes.c_long)
    ]
    type_id = MT_CST_SETTINGS
    type_name = "CST_SETTINGS"


@pyrtma.msg_def
class MDF_NATURAL_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_NATURAL_RESPONSE
    type_name = "NATURAL_RESPONSE"


@pyrtma.msg_def
class MDF_DEPTH_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("idx", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_DEPTH_RESPONSE
    type_name = "DEPTH_RESPONSE"


@pyrtma.msg_def
class MDF_PAIN_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_PAIN_RESPONSE
    type_name = "PAIN_RESPONSE"


@pyrtma.msg_def
class MDF_MODALITY_TOGGLE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_ulong),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_MODALITY_TOGGLE
    type_name = "MODALITY_TOGGLE"


@pyrtma.msg_def
class MDF_MECH_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("idx", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_MECH_RESPONSE
    type_name = "MECH_RESPONSE"


@pyrtma.msg_def
class MDF_MECH_INTENSITY_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_MECH_INTENSITY_RESPONSE
    type_name = "MECH_INTENSITY_RESPONSE"


@pyrtma.msg_def
class MDF_MOVE_INTENSITY_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_MOVE_INTENSITY_RESPONSE
    type_name = "MOVE_INTENSITY_RESPONSE"


@pyrtma.msg_def
class MDF_TINGLE_INTENSITY_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_TINGLE_INTENSITY_RESPONSE
    type_name = "TINGLE_INTENSITY_RESPONSE"


@pyrtma.msg_def
class MDF_MOVE_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("idx", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_MOVE_RESPONSE
    type_name = "MOVE_RESPONSE"


@pyrtma.msg_def
class MDF_DIR_PIXEL_COORDS(pyrtma.MessageData):
    _fields_ = [
        ("img", ctypes.c_char * 32),
        ("moreMsgs", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("pixels", ctypes.c_float * 64)
    ]
    type_id = MT_DIR_PIXEL_COORDS
    type_name = "DIR_PIXEL_COORDS"


@pyrtma.msg_def
class MDF_TINGLE_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("idx", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_TINGLE_RESPONSE
    type_name = "TINGLE_RESPONSE"


@pyrtma.msg_def
class MDF_TEMP_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("a", ctypes.c_float),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_TEMP_RESPONSE
    type_name = "TEMP_RESPONSE"


@pyrtma.msg_def
class MDF_PIXEL_COORDS(pyrtma.MessageData):
    _fields_ = [
        ("img", ctypes.c_char * 32),
        ("moreMsgs", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("pixels", ctypes.c_float * 64)
    ]
    type_id = MT_PIXEL_COORDS
    type_name = "PIXEL_COORDS"


@pyrtma.msg_def
class MDF_STIM_PRES_CONFIG(pyrtma.MessageData):
    _fields_ = [
        ("filename", ctypes.c_char * 256),
        ("randomization", ctypes.c_long)
    ]
    type_id = MT_STIM_PRES_CONFIG
    type_name = "STIM_PRES_CONFIG"


@pyrtma.msg_def
class MDF_STIM_PRESENT(pyrtma.MessageData):
    _fields_ = [
        ("stim_filename", ctypes.c_char * 256),
        ("stim_state_name", ctypes.c_char * 256),
        ("stim_display_time", ctypes.c_double),
        ("stim_start_delay", ctypes.c_double)
    ]
    type_id = MT_STIM_PRESENT
    type_name = "STIM_PRESENT"


@pyrtma.msg_def
class MDF_STIM_PRES_PHASE_END(pyrtma.MessageData):
    _fields_ = [
        ("phase_rep_end", ctypes.c_long)
    ]
    type_id = MT_STIM_PRES_PHASE_END
    type_name = "STIM_PRES_PHASE_END"


@pyrtma.msg_def
class MDF_STIM_PRES_STATUS(pyrtma.MessageData):
    _fields_ = [
        ("pause_resume", ctypes.c_long),
        ("stop", ctypes.c_long)
    ]
    type_id = MT_STIM_PRES_STATUS
    type_name = "STIM_PRES_STATUS"


@pyrtma.msg_def
class MDF_STIM_CONFIG_TYPE(pyrtma.MessageData):
    _fields_ = [
        ("stim_configtype", ctypes.c_char * 128)
    ]
    type_id = MT_STIM_CONFIG_TYPE
    type_name = "STIM_CONFIG_TYPE"


@pyrtma.msg_def
class MDF_GRIP_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("grip_pos", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("velocity", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("force", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("impedance", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("controlMask", ctypes.c_short * 4),
        ("src", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_GRIP_COMMAND
    type_name = "GRIP_COMMAND"


@pyrtma.msg_def
class MDF_GRIP_FINISHED_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("grip_pos", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("velocity", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("force", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("impedance", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("controlMask", ctypes.c_short * 4),
        ("effector", ctypes.c_char * 64)
    ]
    type_id = MT_GRIP_FINISHED_COMMAND
    type_name = "GRIP_FINISHED_COMMAND"


@pyrtma.msg_def
class MDF_GRIPPER_FEEDBACK(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("grip_pos", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("velocity", ctypes.c_double * MAX_GRIPPER_DIMS),
        ("force", ctypes.c_double * MAX_GRIPPER_FORCES),
        ("effector", ctypes.c_char * 64)
    ]
    type_id = MT_GRIPPER_FEEDBACK
    type_name = "GRIPPER_FEEDBACK"


@pyrtma.msg_def
class MDF_MUJOCO_SENSOR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("motor_pos", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("motor_vel", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("motor_torque", ctypes.c_double * MJ_VR_MAX_MOTOR_COUNT),
        ("joint_pos", ctypes.c_double * MJ_VR_MAX_JOINT_COUNT),
        ("joint_vel", ctypes.c_double * MJ_VR_MAX_JOINT_COUNT),
        ("contact", ctypes.c_double * MJ_VR_MAX_CONTACT_COUNT)
    ]
    type_id = MT_MUJOCO_SENSOR
    type_name = "MUJOCO_SENSOR"


@pyrtma.msg_def
class MDF_MUJOCO_CMD(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("ref_pos", ctypes.c_double * MJ_MAX_MOTOR),
        ("ref_vel", ctypes.c_double * MJ_MAX_MOTOR),
        ("gain_pos", ctypes.c_double * MJ_MAX_MOTOR),
        ("gain_vel", ctypes.c_double * MJ_MAX_MOTOR),
        ("ref_pos_enabled", ctypes.c_short),
        ("ref_vel_enabled", ctypes.c_short),
        ("gain_pos_enabled", ctypes.c_short),
        ("gain_vel_enabled", ctypes.c_short)
    ]
    type_id = MT_MUJOCO_CMD
    type_name = "MUJOCO_CMD"


@pyrtma.msg_def
class MDF_MUJOCO_MOVE(pyrtma.MessageData):
    _fields_ = [
        ("mocap_id", ctypes.c_ulong),
        ("link_objects", ctypes.c_ulong),
        ("pos", ctypes.c_double * 3)
    ]
    type_id = MT_MUJOCO_MOVE
    type_name = "MUJOCO_MOVE"


@pyrtma.msg_def
class MDF_MUJOCO_OBJMOVE(pyrtma.MessageData):
    _fields_ = [
        ("obj_id", ctypes.c_ulong),
        ("pos", ctypes.c_double * 3),
        ("orientation", ctypes.c_double * 3)
    ]
    type_id = MT_MUJOCO_OBJMOVE
    type_name = "MUJOCO_OBJMOVE"


@pyrtma.msg_def
class MDF_MUJOCO_MSG(pyrtma.MessageData):
    _fields_ = [
        ("message", ctypes.c_char * 256),
        ("position", ctypes.c_long)
    ]
    type_id = MT_MUJOCO_MSG
    type_name = "MUJOCO_MSG"


@pyrtma.msg_def
class MDF_MUJOCO_GHOST_COLOR(pyrtma.MessageData):
    _fields_ = [
        ("color_id", ctypes.c_double)
    ]
    type_id = MT_MUJOCO_GHOST_COLOR
    type_name = "MUJOCO_GHOST_COLOR"


@pyrtma.msg_def
class MDF_OPENHAND_CMD(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("motor_sp", ctypes.c_ushort * 2),
        ("reserved1", ctypes.c_ushort * 2),
        ("mode", ctypes.c_ubyte),
        ("reserved2", ctypes.c_ubyte * 3)
    ]
    type_id = MT_OPENHAND_CMD
    type_name = "OPENHAND_CMD"


@pyrtma.msg_def
class MDF_OPENHAND_SENS(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("motor_pos", ctypes.c_ushort),
        ("force", ctypes.c_ushort)
    ]
    type_id = MT_OPENHAND_SENS
    type_name = "OPENHAND_SENS"


@pyrtma.msg_def
class MDF_OPTITRACK_RIGID_BODY(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("ID", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("pos", ctypes.c_double * 3),
        ("orient", ctypes.c_double * 3),
        ("timestamp", ctypes.c_double),
        ("name", ctypes.c_char * 128)
    ]
    type_id = MT_OPTITRACK_RIGID_BODY
    type_name = "OPTITRACK_RIGID_BODY"


@pyrtma.msg_def
class MDF_SINGLETACT_DATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("raw_analog", ctypes.c_long * 3),
        ("force", ctypes.c_double * 3)
    ]
    type_id = MT_SINGLETACT_DATA
    type_name = "SINGLETACT_DATA"


class DEKA_CAN_MSG(ctypes.Structure):
    _fields_ = [
        ("can_id", ctypes.c_ulong),
        ("data", ctypes.c_ubyte * 8),
        ("padding", ctypes.c_long)
    ]


@pyrtma.msg_def
class MDF_DEKA_ACI_RESPONSE(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("ACI_1", DEKA_CAN_MSG),
        ("ACI_2", DEKA_CAN_MSG),
        ("ACI_3", DEKA_CAN_MSG)
    ]
    type_id = MT_DEKA_ACI_RESPONSE
    type_name = "DEKA_ACI_RESPONSE"


@pyrtma.msg_def
class MDF_DEKA_SENSOR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("position_msg_1", DEKA_CAN_MSG),
        ("position_msg_2", DEKA_CAN_MSG),
        ("motor_pos", ctypes.c_double * DEKA_DOF_COUNT),
        ("motor_current", ctypes.c_double * DEKA_DOF_COUNT),
        ("mode", ctypes.c_long),
        ("sync", ctypes.c_long),
        ("grip", ctypes.c_long),
        ("padding", ctypes.c_long)
    ]
    type_id = MT_DEKA_SENSOR
    type_name = "DEKA_SENSOR"


@pyrtma.msg_def
class MDF_DEKA_CAN_TOGGLE(pyrtma.MessageData):
    _fields_ = [
        ("toggle", ctypes.c_long),
        ("padding", ctypes.c_long)
    ]
    type_id = MT_DEKA_CAN_TOGGLE
    type_name = "DEKA_CAN_TOGGLE"


@pyrtma.msg_def
class MDF_DEKA_CAN_GRIP_TOGGLE(pyrtma.MessageData):
    _fields_ = [
        ("toggle", ctypes.c_long),
        ("padding", ctypes.c_long)
    ]
    type_id = MT_DEKA_CAN_GRIP_TOGGLE
    type_name = "DEKA_CAN_GRIP_TOGGLE"


@pyrtma.msg_def
class MDF_DEKA_CAN_EXIT(pyrtma.MessageData):
    _fields_ = [
        ("exit", ctypes.c_long),
        ("padding", ctypes.c_long)
    ]
    type_id = MT_DEKA_CAN_EXIT
    type_name = "DEKA_CAN_EXIT"


@pyrtma.msg_def
class MDF_KUKA_JOINT_COMMAND(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("joint_dest", ctypes.c_double * KUKA_DOF_COUNT),
        ("err_move_mode", ctypes.c_long),
        ("err_input_cap", ctypes.c_long * 6),
        ("err_cart_wall_eef", ctypes.c_long * 6),
        ("err_cart_wall_arm", ctypes.c_long * 6),
        ("err_jpos_stop", ctypes.c_long * 3)
    ]
    type_id = MT_KUKA_JOINT_COMMAND
    type_name = "KUKA_JOINT_COMMAND"


@pyrtma.msg_def
class MDF_KUKA_FEEDBACK(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("time", ctypes.c_double),
        ("joint_pos", ctypes.c_double * KUKA_DOF_COUNT),
        ("cart_pos", ctypes.c_double * 3),
        ("cart_angle", ctypes.c_double * 3),
        ("cart_pos_vel", ctypes.c_double * 3),
        ("cart_rot_vel", ctypes.c_double * 3),
        ("cart_force", ctypes.c_double * 3),
        ("cart_torque", ctypes.c_double * 3),
        ("dest_delta_t", ctypes.c_double),
        ("mode", ctypes.c_long),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_KUKA_FEEDBACK
    type_name = "KUKA_FEEDBACK"


@pyrtma.msg_def
class MDF_KUKA_EXIT(pyrtma.MessageData):
    _fields_ = [
        ("exit", ctypes.c_long),
        ("padding", ctypes.c_long)
    ]
    type_id = MT_KUKA_EXIT
    type_name = "KUKA_EXIT"


@pyrtma.msg_def
class MDF_KUKA_PTP_JOINT(pyrtma.MessageData):
    _fields_ = [
        ("joint_pos", ctypes.c_double * KUKA_DOF_COUNT)
    ]
    type_id = MT_KUKA_PTP_JOINT
    type_name = "KUKA_PTP_JOINT"


@pyrtma.msg_def
class MDF_KUKA_DEBUG(pyrtma.MessageData):
    _fields_ = [
        ("joint_pos", ctypes.c_double * KUKA_DOF_COUNT)
    ]
    type_id = MT_KUKA_DEBUG
    type_name = "KUKA_DEBUG"


@pyrtma.msg_def
class MDF_XIPP_EMG_DATA_RAW(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("num_chans_per_headstage", ctypes.c_long * MAX_XIPP_EEG_HEADSTAGES),
        ("source_timestamp", ctypes.c_ulong * XIPP_SAMPLES_PER_MSG),
        ("data", ctypes.c_float * int(XIPP_SAMPLES_PER_MSG * MAX_XIPP_CHANS))
    ]
    type_id = MT_XIPP_EMG_DATA_RAW
    type_name = "XIPP_EMG_DATA_RAW"


@pyrtma.msg_def
class MDF_MYO_EMG_DATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_ulonglong * MYO_SAMPLES_PER_MSG),
        ("data", ctypes.c_long * int(MYO_SAMPLES_PER_MSG * MAX_MYO_EMG_CHANS))
    ]
    type_id = MT_MYO_EMG_DATA
    type_name = "MYO_EMG_DATA"


@pyrtma.msg_def
class MDF_MYO_KIN_DATA(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_ulonglong),
        ("orientation", ctypes.c_float * 4),
        ("gyroscope", ctypes.c_float * 3),
        ("acceleration", ctypes.c_float * 3)
    ]
    type_id = MT_MYO_KIN_DATA
    type_name = "MYO_KIN_DATA"


@pyrtma.msg_def
class MDF_SAMPLE_GENERATED(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("source_timestamp", ctypes.c_double),
        ("xipp_timestamp", ctypes.c_ulong),
        ("reserved", ctypes.c_long)
    ]
    type_id = MT_SAMPLE_GENERATED
    type_name = "SAMPLE_GENERATED"


@pyrtma.msg_def
class MDF_PRENSILIA_SENS(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("stream_type", ctypes.c_ushort),
        ("current", ctypes.c_ushort * PRENSILIA_DOF),
        ("position", ctypes.c_ushort * PRENSILIA_DOF),
        ("external", ctypes.c_ushort * PRENSILIA_EXT_SENSORS),
        ("tension", ctypes.c_ushort * PRENSILIA_DOF),
        ("reserved", ctypes.c_ushort)
    ]
    type_id = MT_PRENSILIA_SENS
    type_name = "PRENSILIA_SENS"


@pyrtma.msg_def
class MDF_PRENSILIA_CMD(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("mode", ctypes.c_short * PRENSILIA_DOF),
        ("command", ctypes.c_short * PRENSILIA_DOF)
    ]
    type_id = MT_PRENSILIA_CMD
    type_name = "PRENSILIA_CMD"


@pyrtma.msg_def
class MDF_DEKA_HAND_SENSOR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("position_msg_1", DEKA_CAN_MSG),
        ("position_msg_2", DEKA_CAN_MSG),
        ("force_msg_1", DEKA_CAN_MSG),
        ("force_msg_2", DEKA_CAN_MSG),
        ("force_msg_3", DEKA_CAN_MSG),
        ("motor_pos", ctypes.c_double * HX_LUKE_MOTOR_COUNT),
        ("contact", ctypes.c_double * HX_DEKA_LUKE_CONTACT_COUNT),
        ("mode", ctypes.c_long),
        ("status", ctypes.c_long * HX_DEKA_LUKE_CONTACT_COUNT),
        ("sync", ctypes.c_long),
        ("grip", ctypes.c_long)
    ]
    type_id = MT_DEKA_HAND_SENSOR
    type_name = "DEKA_HAND_SENSOR"


@pyrtma.msg_def
class MDF_DEKA_HAND_JSTICK_CMD(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("ref_vel", ctypes.c_double * HX_LUKE_MOTOR_COUNT)
    ]
    type_id = MT_DEKA_HAND_JSTICK_CMD
    type_name = "DEKA_HAND_JSTICK_CMD"


class RH_FINGER_DATA(ctypes.Structure):
    _fields_ = [
        ("proximal_angle", ctypes.c_float),
        ("distal_angle", ctypes.c_float),
        ("pressure", ctypes.c_float * NUM_SENSORS_PER_FINGER),
        ("contact", ctypes.c_long * NUM_SENSORS_PER_FINGER)
    ]


class DYNAMIXEL_INFO(ctypes.Structure):
    _fields_ = [
        ("joint_angle", ctypes.c_float * NUM_DYNAMIXEL),
        ("raw_angle", ctypes.c_float * NUM_DYNAMIXEL),
        ("velocity", ctypes.c_float * NUM_DYNAMIXEL),
        ("load", ctypes.c_float * NUM_DYNAMIXEL),
        ("voltage", ctypes.c_float * NUM_DYNAMIXEL),
        ("temperature", ctypes.c_long * NUM_DYNAMIXEL)
    ]


@pyrtma.msg_def
class MDF_RH_GRIPPER_SENSOR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("finger_1", RH_FINGER_DATA),
        ("finger_2", RH_FINGER_DATA),
        ("finger_3", RH_FINGER_DATA),
        ("motor_info", DYNAMIXEL_INFO)
    ]
    type_id = MT_RH_GRIPPER_SENSOR
    type_name = "RH_GRIPPER_SENSOR"


@pyrtma.msg_def
class MDF_TABLE_LOAD_CELLS(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("left_plate", ctypes.c_double * 4),
        ("left_plate_mean", ctypes.c_double),
        ("center_plate", ctypes.c_double * 4),
        ("center_plate_mean", ctypes.c_double),
        ("right_plate", ctypes.c_double * 4),
        ("right_plate_mean", ctypes.c_double)
    ]
    type_id = MT_TABLE_LOAD_CELLS
    type_name = "TABLE_LOAD_CELLS"


@pyrtma.msg_def
class MDF_TASKA_CMD(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("op_code", ctypes.c_ubyte),
        ("padding", ctypes.c_ubyte * 7),
        ("stx", ctypes.c_ubyte),
        ("type", ctypes.c_ubyte),
        ("sub_index", ctypes.c_ubyte),
        ("length", ctypes.c_ubyte),
        ("data", ctypes.c_ubyte * 60)
    ]
    type_id = MT_TASKA_CMD
    type_name = "TASKA_CMD"


@pyrtma.msg_def
class MDF_TASKA_REPLY(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("tx_timestamp", ctypes.c_double),
        ("rx_timestamp", ctypes.c_double),
        ("comm_time", ctypes.c_double),
        ("op_code", ctypes.c_ubyte),
        ("padding", ctypes.c_ubyte * 7),
        ("stx", ctypes.c_ubyte),
        ("type", ctypes.c_ubyte),
        ("sub_index", ctypes.c_ubyte),
        ("length", ctypes.c_ubyte),
        ("data", ctypes.c_ubyte * 60)
    ]
    type_id = MT_TASKA_REPLY
    type_name = "TASKA_REPLY"


@pyrtma.msg_def
class MDF_TASKA_ERROR(pyrtma.MessageData):
    _fields_ = [
        ("header", MSG_HEADER),
        ("error_code", ctypes.c_long),
        ("reserved", ctypes.c_long),
        ("msg", ctypes.c_char * 256),
        ("dump", ctypes.c_ubyte * 64)
    ]
    type_id = MT_TASKA_ERROR
    type_name = "TASKA_ERROR"


@pyrtma.msg_def
class MDF_MECH_STIM_CONFIGURE(pyrtma.MessageData):
    _fields_ = [
        ("source", ctypes.c_long),
        ("length", ctypes.c_long),
        ("str", ctypes.c_char * 1024)
    ]
    type_id = MT_MECH_STIM_CONFIGURE
    type_name = "MECH_STIM_CONFIGURE"


# Signal Definition
@pyrtma.msg_def
class MDF_MUJOCO_VR_RESET(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MUJOCO_VR_RESET
    type_name = "MUJOCO_VR_RESET"


# Signal Definition
@pyrtma.msg_def
class MDF_MUJOCO_VR_RELOAD(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MUJOCO_VR_RELOAD
    type_name = "MUJOCO_VR_RELOAD"


# Signal Definition
@pyrtma.msg_def
class MDF_MUJOCO_VR_PAUSE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MUJOCO_VR_PAUSE
    type_name = "MUJOCO_VR_PAUSE"


# Signal Definition
@pyrtma.msg_def
class MDF_MUJOCO_VR_RESUME(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MUJOCO_VR_RESUME
    type_name = "MUJOCO_VR_RESUME"


# Signal Definition
@pyrtma.msg_def
class MDF_CONTROL_SPACE_FEEDBACK_RHR_GRIPPER(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_CONTROL_SPACE_FEEDBACK_RHR_GRIPPER
    type_name = "CONTROL_SPACE_FEEDBACK_RHR_GRIPPER"


# Signal Definition
@pyrtma.msg_def
class MDF_REZERO_GRIPPER_SENSORS(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_REZERO_GRIPPER_SENSORS
    type_name = "REZERO_GRIPPER_SENSORS"


# Signal Definition
@pyrtma.msg_def
class MDF_EXTRACTION_REQUEST(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_EXTRACTION_REQUEST
    type_name = "EXTRACTION_REQUEST"


# Signal Definition
@pyrtma.msg_def
class MDF_TRIAL_END(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_TRIAL_END
    type_name = "TRIAL_END"


# Signal Definition
@pyrtma.msg_def
class MDF_REP_END(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_REP_END
    type_name = "REP_END"


# Signal Definition
@pyrtma.msg_def
class MDF_EM_ADAPT_NOW(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_EM_ADAPT_NOW
    type_name = "EM_ADAPT_NOW"


# Signal Definition
@pyrtma.msg_def
class MDF_TACTOR_CMD(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_TACTOR_CMD
    type_name = "TACTOR_CMD"


# Signal Definition
@pyrtma.msg_def
class MDF_AJA_STATUS_REQUEST(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_AJA_STATUS_REQUEST
    type_name = "AJA_STATUS_REQUEST"


# Signal Definition
@pyrtma.msg_def
class MDF_CERESTIM_ALIVE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_CERESTIM_ALIVE
    type_name = "CERESTIM_ALIVE"


# Signal Definition
@pyrtma.msg_def
class MDF_CS_TRAIN_END(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_CS_TRAIN_END
    type_name = "CS_TRAIN_END"


# Signal Definition
@pyrtma.msg_def
class MDF_CS_ARBITRARY_CLOSE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_CS_ARBITRARY_CLOSE
    type_name = "CS_ARBITRARY_CLOSE"


# Signal Definition
@pyrtma.msg_def
class MDF_CLEAR_LINE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_CLEAR_LINE
    type_name = "CLEAR_LINE"


# Signal Definition
@pyrtma.msg_def
class MDF_ADD_SENSATION(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_ADD_SENSATION
    type_name = "ADD_SENSATION"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_RESET(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_RESET
    type_name = "MECH_STIM_RESET"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_STAGE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_STAGE
    type_name = "MECH_STIM_STAGE"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_WAITING(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_WAITING
    type_name = "MECH_STIM_WAITING"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_TRIGGER(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_TRIGGER
    type_name = "MECH_STIM_TRIGGER"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_CANCEL(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_CANCEL
    type_name = "MECH_STIM_CANCEL"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_DONE(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_DONE
    type_name = "MECH_STIM_DONE"


# Signal Definition
@pyrtma.msg_def
class MDF_MECH_STIM_ERROR(pyrtma.MessageData):
    _fields_ = []
    type_id = MT_MECH_STIM_ERROR
    type_name = "MECH_STIM_ERROR"

