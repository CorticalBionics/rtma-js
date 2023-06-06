export { RTMA } ;

// RTMA Constants
const MAX_MODULES= 200;
const DYN_MOD_ID_START= 100;
const MAX_HOSTS= 5;
const MAX_MESSAGE_TYPES= 10000;
const MIN_STREAM_TYPE= 9000;
const MAX_TIMERS= 100;
const MAX_INTERNAL_TIMERS= 20;
const MAX_RTMA_MSG_TYPE= 99;
const MAX_RTMA_MODULE_ID= 9;
const MAX_LOGGER_FILENAME_LENGTH= 256;
const MAX_CONTIGUOUS_MESSAGE_DATA= 9000;
const HID_LOCAL_HOST= 0;
const HID_ALL_HOSTS= 0x7FFF;
const ALL_MESSAGE_TYPES= 0x7FFFFFFF;
const MJ_VR_MAX_MOCAP_COUNT= 32;
const MJ_VR_MAX_BODY_COUNT= 64;
const MJ_VR_MAX_MOTOR_COUNT= 32;
const MJ_VR_MAX_JOINT_COUNT= 64;
const MJ_VR_MAX_JOINT_DOF= 128;
const MJ_VR_MAX_CONTACT_COUNT= 32;
const MJ_VR_MAX_TENDON_COUNT= 32;
const MAX_SPIKE_SOURCES= 2;
const MAX_SPIKE_SOURCES_N256= 1;
const MAX_SPIKE_CHANS_PER_SOURCE= 128;
const MAX_SPIKE_CHANS_PER_SOURCE_N256= 256;
const MAX_COINCIDENT_SPIKES= 45;
const MAX_ANALOG_CHANS= 16;
const MAX_UNITS_PER_CHAN= 5;
const MAX_TOTAL_SPIKE_CHANS_PER_SOURCE= (MAX_SPIKE_CHANS_PER_SOURCE * MAX_UNITS_PER_CHAN);
const MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256= (MAX_SPIKE_CHANS_PER_SOURCE_N256 * MAX_UNITS_PER_CHAN);
const MAX_TOTAL_SPIKE_CHANS= (MAX_SPIKE_SOURCES * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE);
const MAX_TOTAL_SPIKE_CHANS_N256= (MAX_SPIKE_SOURCES_N256 * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256);
const LFPSAMPLES_PER_HEARTBEAT= 10;
const ANALOGSAMPLES_PER_HEARTBEAT= 10;
const RAW_COUNTS_PER_SAMPLE= 2;
const SAMPLE_LENGTH= (0.01 * RAW_COUNTS_PER_SAMPLE);
const SNIPPETS_PER_MESSAGE= 25;
const SAMPLES_PER_SNIPPET= 48;
const MAX_DIG_PER_SAMPLE= 10;
const MAX_DATAGLOVE_SENSORS= 18;
const NUM_DOMAINS= 6;
const MAX_COMMAND_DIMS= 30;
const MPL_RAW_PERCEPT_DIMS= 54;
const NUM_STIM_CHANS= 64;
const SHAM_STIM_CHANS= 32;
const MAX_STIM_CHANS_ON= 12;
const PULSE_TRAIN_SIZE= 101;
const MAX_CS_CONFIGS= 16;
const NUM_SPIKES_PER_STIM_MSG= 26;
const MAX_XIPP_EEG_HEADSTAGES= 2;
const MAX_XIPP_CHANS= 32 * MAX_XIPP_EEG_HEADSTAGES;
const MAX_XIPP_ANALOG_CHANS= 32;
const XIPP_SAMPLES_PER_MSG= 20;
const MAX_MYO_EMG_CHANS= 8;
const MYO_SAMPLES_PER_MSG= 4;
const GRIP_DIMS_R= 1;
const GRIP_DIMS_L= 1;
const MAX_GRIP_DIMS= 9;
const MAX_GRIPPER_DIMS= 1;
const MAX_GRIPPER_JOINT_ANGLES= 5;
const MAX_GRIPPER_FORCES= 5;
const MJ_MAX_MOTOR= MAX_GRIPPER_DIMS;
const MJ_MAX_JOINT= MAX_GRIPPER_JOINT_ANGLES;
const MJ_MAX_CONTACT= MAX_GRIPPER_FORCES;
const NoResult= -1;
const SuccessfulTrial= 1;
const BadTrial= 2;
const ManualProceed= 4;
const ManualFail= 8;
const HX_DEKA_LUKE_CONTACT_COUNT= 13;
const HX_LUKE_MOTOR_COUNT= 6;
const NUM_FINGERS= 3;
const NUM_SENSORS_PER_FINGER= 9;
const NUM_SENSORS_PALM= 11;
const NUM_TAKKTILE= (NUM_FINGERS * NUM_SENSORS_PER_FINGER + NUM_SENSORS_PALM);
const NUM_ENCODERS= NUM_FINGERS;
const NUM_SERVOS= 4;
const NUM_DYNAMIXEL= NUM_SERVOS;
const DEKA_DOF_COUNT= 7;
const KUKA_DOF_COUNT= 7;
const TAG_LENGTH= 64;
const MPL_AT_ARM_EPV_FING_JV= 0;
const MPL_AT_ARM_EPV_FING_JP= 1;
const MPL_AT_ARM_JV_FING_JP= 2;
const MPL_AT_ALL_JV= 3;
const MPL_AT_ALL_JP= 4;
const MPL_AT_ARM_EPP_FING_JP= 5;
const TFD_FREQ_BINS= 20;
const MUJOCO_LINK_ID= 1000;
const PRENSILIA_DOF= 5;
const PRENSILIA_EXT_SENSORS= 7;

const RTMA = {
	constants: {
		MAX_MODULES: 200,
		DYN_MOD_ID_START: 100,
		MAX_HOSTS: 5,
		MAX_MESSAGE_TYPES: 10000,
		MIN_STREAM_TYPE: 9000,
		MAX_TIMERS: 100,
		MAX_INTERNAL_TIMERS: 20,
		MAX_RTMA_MSG_TYPE: 99,
		MAX_RTMA_MODULE_ID: 9,
		MAX_LOGGER_FILENAME_LENGTH: 256,
		MAX_CONTIGUOUS_MESSAGE_DATA: 9000,
		HID_LOCAL_HOST: 0,
		HID_ALL_HOSTS: 0x7FFF,
		ALL_MESSAGE_TYPES: 0x7FFFFFFF,
		MJ_VR_MAX_MOCAP_COUNT: 32,
		MJ_VR_MAX_BODY_COUNT: 64,
		MJ_VR_MAX_MOTOR_COUNT: 32,
		MJ_VR_MAX_JOINT_COUNT: 64,
		MJ_VR_MAX_JOINT_DOF: 128,
		MJ_VR_MAX_CONTACT_COUNT: 32,
		MJ_VR_MAX_TENDON_COUNT: 32,
		MAX_SPIKE_SOURCES: 2,
		MAX_SPIKE_SOURCES_N256: 1,
		MAX_SPIKE_CHANS_PER_SOURCE: 128,
		MAX_SPIKE_CHANS_PER_SOURCE_N256: 256,
		MAX_COINCIDENT_SPIKES: 45,
		MAX_ANALOG_CHANS: 16,
		MAX_UNITS_PER_CHAN: 5,
		MAX_TOTAL_SPIKE_CHANS_PER_SOURCE: (MAX_SPIKE_CHANS_PER_SOURCE * MAX_UNITS_PER_CHAN),
		MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256: (MAX_SPIKE_CHANS_PER_SOURCE_N256 * MAX_UNITS_PER_CHAN),
		MAX_TOTAL_SPIKE_CHANS: (MAX_SPIKE_SOURCES * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE),
		MAX_TOTAL_SPIKE_CHANS_N256: (MAX_SPIKE_SOURCES_N256 * MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256),
		LFPSAMPLES_PER_HEARTBEAT: 10,
		ANALOGSAMPLES_PER_HEARTBEAT: 10,
		RAW_COUNTS_PER_SAMPLE: 2,
		SAMPLE_LENGTH: (0.01 * RAW_COUNTS_PER_SAMPLE),
		SNIPPETS_PER_MESSAGE: 25,
		SAMPLES_PER_SNIPPET: 48,
		MAX_DIG_PER_SAMPLE: 10,
		MAX_DATAGLOVE_SENSORS: 18,
		NUM_DOMAINS: 6,
		MAX_COMMAND_DIMS: 30,
		MPL_RAW_PERCEPT_DIMS: 54,
		NUM_STIM_CHANS: 64,
		SHAM_STIM_CHANS: 32,
		MAX_STIM_CHANS_ON: 12,
		PULSE_TRAIN_SIZE: 101,
		MAX_CS_CONFIGS: 16,
		NUM_SPIKES_PER_STIM_MSG: 26,
		MAX_XIPP_EEG_HEADSTAGES: 2,
		MAX_XIPP_CHANS: 32 * MAX_XIPP_EEG_HEADSTAGES,
		MAX_XIPP_ANALOG_CHANS: 32,
		XIPP_SAMPLES_PER_MSG: 20,
		MAX_MYO_EMG_CHANS: 8,
		MYO_SAMPLES_PER_MSG: 4,
		GRIP_DIMS_R: 1,
		GRIP_DIMS_L: 1,
		MAX_GRIP_DIMS: 9,
		MAX_GRIPPER_DIMS: 1,
		MAX_GRIPPER_JOINT_ANGLES: 5,
		MAX_GRIPPER_FORCES: 5,
		MJ_MAX_MOTOR: MAX_GRIPPER_DIMS,
		MJ_MAX_JOINT: MAX_GRIPPER_JOINT_ANGLES,
		MJ_MAX_CONTACT: MAX_GRIPPER_FORCES,
		NoResult: -1,
		SuccessfulTrial: 1,
		BadTrial: 2,
		ManualProceed: 4,
		ManualFail: 8,
		HX_DEKA_LUKE_CONTACT_COUNT: 13,
		HX_LUKE_MOTOR_COUNT: 6,
		NUM_FINGERS: 3,
		NUM_SENSORS_PER_FINGER: 9,
		NUM_SENSORS_PALM: 11,
		NUM_TAKKTILE: (NUM_FINGERS * NUM_SENSORS_PER_FINGER + NUM_SENSORS_PALM),
		NUM_ENCODERS: NUM_FINGERS,
		NUM_SERVOS: 4,
		NUM_DYNAMIXEL: NUM_SERVOS,
		DEKA_DOF_COUNT: 7,
		KUKA_DOF_COUNT: 7,
		TAG_LENGTH: 64,
		MPL_AT_ARM_EPV_FING_JV: 0,
		MPL_AT_ARM_EPV_FING_JP: 1,
		MPL_AT_ARM_JV_FING_JP: 2,
		MPL_AT_ALL_JV: 3,
		MPL_AT_ALL_JP: 4,
		MPL_AT_ARM_EPP_FING_JP: 5,
		TFD_FREQ_BINS: 20,
		MUJOCO_LINK_ID: 1000,
		PRENSILIA_DOF: 5,
		PRENSILIA_EXT_SENSORS: 7,
	},

	MT: {
		EXIT: 0,
		KILL: 1,
		ACKNOWLEDGE: 2,
		CONNECT: 13,
		DISCONNECT: 14,
		SUBSCRIBE: 15,
		UNSUBSCRIBE: 16,
		PAUSE_SUBSCRIPTION: 85,
		FAIL_SUBSCRIBE: 6,
		FAILED_MESSAGE: 8,
		FORCED_DISCONNECT: 82,
		MODULE_READY: 26,
		SAVE_MESSAGE_LOG: 56,
		TIMING_MESSAGE: 80,
		MUJOCO_VR_REQUEST_STATE: 4213,
		MUJOCO_VR_REPLY_STATE: 4214,
		MUJOCO_VR_MOCAP_MOVE: 4215,
		MUJOCO_VR_MOTOR_MOVE: 4216,
		MUJOCO_VR_REQUEST_MODEL_INFO: 4217,
		MUJOCO_VR_REPLY_MODEL_INFO: 4218,
		MUJOCO_VR_REQUEST_LINK_STATE: 4219,
		MUJOCO_VR_REPLY_LINK_STATE: 4220,
		MUJOCO_VR_LINK: 4221,
		MUJOCO_VR_LINK_RESET: 4222,
		MUJOCO_VR_FLOATBODY_MOVE: 4223,
		MUJOCO_VR_RESET: 4224,
		MUJOCO_VR_RELOAD: 4225,
		MUJOCO_VR_LOAD_MODEL: 4226,
		MUJOCO_VR_PAUSE: 4227,
		MUJOCO_VR_RESUME: 4228,
		MUJOCO_VR_MOTOR_CTRL: 4229,
		MUJOCO_VR_MOTOR_CONFIG: 4230,
		MUJOCO_VR_SET_RGBA: 4231,
		MUJOCO_VR_MSG: 4232,
		FINISHED_COMMAND: 1700,
		CONTROL_SPACE_FEEDBACK: 1701,
		CONTROL_SPACE_COMMAND: 1702,
		MPL_RAW_PERCEPT: 1703,
		BIAS_COMMAND: 1704,
		MPL_REBIASED_SENSORDATA: 1705,
		CONTROL_SPACE_FEEDBACK_RHR_GRIPPER: 1706,
		CONTROL_SPACE_POS_COMMAND: 1710,
		MPL_SEGMENT_PERCEPTS: 1711,
		WAM_FEEDBACK: 1712,
		IMPEDANCE_COMMAND: 1713,
		EXECUTIVE_CTRL: 1714,
		CURSOR_FEEDBACK: 1720,
		VISUAL_GRATING_BUILD: 1721,
		VISUAL_GRATING_RESPONSE: 1722,
		GRIP_COMMAND: 1730,
		GRIP_FINISHED_COMMAND: 1731,
		GRIPPER_FEEDBACK: 1732,
		MUJOCO_SENSOR: 1733,
		MUJOCO_CMD: 1734,
		MUJOCO_MOVE: 1735,
		MUJOCO_MSG: 1736,
		MUJOCO_GHOST_COLOR: 1737,
		MUJOCO_OBJMOVE: 1738,
		OPENHAND_CMD: 1740,
		OPENHAND_SENS: 1741,
		PRENSILIA_SENS: 1742,
		PRENSILIA_CMD: 1743,
		TABLE_LOAD_CELLS: 1744,
		REZERO_GRIPPER_SENSORS: 1745,
		SINGLETACT_DATA: 1760,
		RAW_SPIKECOUNT: 1800,
		SPM_SPIKECOUNT: 1801,
		SPIKE_SNIPPET: 1802,
		RAW_CTSDATA: 1803,
		SPM_CTSDATA: 1804,
		REJECTED_SNIPPET: 1805,
		RAW_DIGITAL_EVENT: 1806,
		SPM_DIGITAL_EVENT: 1807,
		STIM_SYNC_EVENT: 1808,
		STIM_UPDATE_EVENT: 1809,
		CENTRALRECORD: 1810,
		RAW_ANALOGDATA: 1811,
		SPM_ANALOGDATA: 1812,
		RAW_SPIKECOUNT_N256: 1815,
		RAW_CTSDATA_N256: 1816,
		SAMPLE_GENERATED: 1820,
		XIPP_EMG_DATA_RAW: 1830,
		MYO_EMG_DATA: 1831,
		MYO_KIN_DATA: 1832,
		INPUT_DOF_DATA: 1850,
		DATAGLOVE: 1860,
		OPTITRACK_RIGID_BODY: 1861,
		TASK_STATE_CONFIG: 1900,
		PHASE_RESULT: 1901,
		EXTRACTION_RESPONSE: 1902,
		NORMALIZATION_FACTOR: 1903,
		TRIAL_METADATA: 1904,
		EXTRACTION_REQUEST: 1905,
		UPDATE_UNIT_STATE: 1906,
		DISABLED_UNITS: 1907,
		TRIAL_END: 1910,
		REP_START: 1911,
		REP_END: 1912,
		EXEC_SCORE: 1913,
		FLIP_THAT_BUCKET_DATA: 1914,
		EM_ADAPT_NOW: 2000,
		EM_CONFIGURATION: 2001,
		TDMS_CREATE: 2002,
		RF_REPORT: 2003,
		PICDISPLAY: 2004,
		STIMDATA: 2005,
		SEAIO_OUT: 2007,
		ATIforcesensor: 2008,
		TACTOR_CMD: 2009,
		HSTLOG: 3000,
		PLAYSOUND: 3100,
		PLAYVIDEO: 3102,
		START_TIMED_RECORDING: 3101,
		AJA_CONFIG: 3200,
		AJA_TIMECODE: 3201,
		AJA_STATUS: 3202,
		AJA_STATUS_REQUEST: 3203,
		CERESTIM_CONFIG_MODULE: 4000,
		CERESTIM_CONFIG_CHAN_PRESAFETY: 4001,
		CERESTIM_CONFIG_CHAN: 4002,
		CERESTIM_ERROR: 4003,
		CERESTIM_ALIVE: 4004,
		CS_TRAIN_END: 4005,
		CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY: 4006,
		CERESTIM_CONFIG_CHAN_ARBITRARY: 4007,
		CS_ARBITRARY_CLOSE: 4008,
		STIM_VOLTAGE_MONITOR_DATA: 4009,
		STIM_VOLTAGE_MONITOR_DIGITAL_DATA: 4010,
		VOLTAGE_MONITOR_STATUS: 4011,
		STIM_DUTYCYCLE_TIME: 4012,
		STIM_TRIAL_DURATION: 4013,
		NATURAL_RESPONSE: 4050,
		DEPTH_RESPONSE: 4051,
		PAIN_RESPONSE: 4052,
		MODALITY_TOGGLE: 4053,
		MECH_RESPONSE: 4054,
		MECH_INTENSITY_RESPONSE: 4055,
		MOVE_RESPONSE: 4056,
		MOVE_INTENSITY_RESPONSE: 4057,
		TINGLE_RESPONSE: 4058,
		TINGLE_INTENSITY_RESPONSE: 4059,
		TEMP_RESPONSE: 4060,
		DIR_PIXEL_COORDS: 4061,
		PIXEL_COORDS: 4063,
		CLEAR_LINE: 4064,
		ADD_SENSATION: 4065,
		SLIDER_DATA: 4066,
		USER_DEFINED_STIM: 4067,
		USER_BEHAVIOUR: 4068,
		STOP_STIM: 4069,
		PAUSE_TRIAL: 4070,
		CST_LAMBDA: 4100,
		CST_SETTINGS: 4101,
		STIM_PRES_CONFIG: 4150,
		STIM_PRES_PHASE_END: 4151,
		STIM_PRESENT: 4152,
		STIM_PRES_STATUS: 4153,
		STIM_CONFIG_TYPE: 4154,
		DEKA_ACI_RESPONSE: 4200,
		DEKA_SENSOR: 4201,
		DEKA_CAN_TOGGLE: 4202,
		DEKA_CAN_GRIP_TOGGLE: 4203,
		DEKA_CAN_EXIT: 4204,
		DEKA_HAND_SENSOR: 4205,
		DEKA_HAND_JSTICK_CMD: 4206,
		RH_GRIPPER_SENSOR: 4207,
		KUKA_JOINT_COMMAND: 4208,
		KUKA_FEEDBACK: 4209,
		KUKA_EXIT: 4210,
		KUKA_PTP_JOINT: 4211,
		KUKA_DEBUG: 4212,
		TASKA_CMD: 4250,
		TASKA_REPLY: 4251,
		TASKA_ERROR: 4252,
		MECH_STIM_CONFIGURE: 4240,
		MECH_STIM_RESET: 4241,
		MECH_STIM_STAGE: 4242,
		MECH_STIM_WAITING: 4243,
		MECH_STIM_TRIGGER: 4244,
		MECH_STIM_CANCEL: 4245,
		MECH_STIM_DONE: 4246,
		MECH_STIM_ERROR: 4247,
	},

	MID: {
		MESSAGE_MANAGER: 0,
		COMMAND_MODULE: 1,
		APPLICATION_MODULE: 2,
		NETWORK_RELAY: 3,
		STATUS_MODULE: 4,
		QUICKLOGGER: 5,
		MUJOCO_VR_MODULE: 61,
		JSTICK_COMMAND: 10,
		COMBINER: 11,
		CEREBUS: 12,
		INPUT_TRANSFORM: 20,
		RPPL_RECORD: 21,
		CENTRAL: 22,
		EXTRACTION: 30,
		MYO: 31,
		MPL_CONTROL: 40,
		GRIP_CONTROL: 41,
		DEKA_CAN_MODULE: 42,
		DEKA_ACI_RESPONSE: 43,
		DEKA_DISPLAY: 44,
		PSYCHTLBX: 46,
		STIM_PRESENT: 48,
		ACTIVE_ASSIST: 50,
		KUKA_DISPLAY: 51,
		ROBOTICS_FEEDBACK_INTEGRATOR: 52,
		KUKA_INTERFACE_MODULE: 53,
		KUKA_JOINT_COMMAND_DISPLAY: 54,
		KUKA_DIAGNOSTICS: 55,
		TASKA_DRIVER: 56,
		FORCE_PLATFORM: 58,
		FORCE_PLATFORM_DISPLAY: 59,
		MPL_FEEDBACK: 60,
		AJA_CONTROL: 65,
		SEAIOCONTROL: 66,
		EXECUTIVE: 70,
		COMMENT_MANAGER: 71,
		FLIP_THAT_BUCKET_MESSENGER: 74,
		VOLTAGE_MONITOR_GUI: 76,
		VOLTAGE_MONITOR: 77,
		ATIsensor: 78,
		MESSAGERATES: 81,
		VISUAL_GRATING: 85,
		BIASMODULE: 86,
		CURSOR: 87,
		RHR_COMMAND_MODULE: 88,
		RHR_SENSOR_MODULE: 89,
		SOUNDPLAYER: 90,
		RFDISPLAY: 91,
		RFACTIVITY: 92,
		ImageDisplayer: 93,
		FLIP_THAT_BUCKET: 94,
		STIM_SAFETY_MODULE: 95,
		SENSOR_STIM_TRANS_MODULE: 96,
		CERESTIM_CONTROL: 97,
		SENSE_TOUCH_INTERFACE: 98,
		SENSOR_STIM_TRANSFORM_PY: 99,
		MECH_STIM_MODULE: 0,
	},

	MDF : {
		RTMA_MSG_HEADER: () => {
			return {
				msg_type: 0,
				msg_count: 0,
				send_time: 0,
				recv_time: 0,
				src_host_id: 0,
				src_mod_id: 0,
				dest_host_id: 0,
				dest_mod_id: 0,
				num_data_bytes: 0,
				remaining_bytes: 0,
				is_dynamic: 0,
				reserved: 0,
			}
		},

		CONNECT: () => {
			return {
				logger_status: 0,
				daemon_status: 0,
			}
		},

		SUBSCRIBE: () => {
			return {
				msg_type: 0,
			}
		},

		UNSUBSCRIBE: () => {
			return {
				msg_type: 0,
			}
		},

		PAUSE_SUBSCRIPTION: () => {
			return {
				msg_type: 0,
			}
		},

		RESUME_SUBSCRIPTION: () => {
			return {
				msg_type: 0,
			}
		},

		FAIL_SUBSCRIBE: () => {
			return {
				mod_id: 0,
				reserved: 0,
				msg_type: 0,
			}
		},

		FAILED_MESSAGE: () => {
			return {
				dest_mod_id: 0,
				reserved: 0,
				time_of_failure: 0,
				msg_header: {
					msg_type: 0,
					msg_count: 0,
					send_time: 0,
					recv_time: 0,
					src_host_id: 0,
					src_mod_id: 0,
					dest_host_id: 0,
					dest_mod_id: 0,
					num_data_bytes: 0,
					remaining_bytes: 0,
					is_dynamic: 0,
					reserved: 0,
				},
			}
		},

		FORCE_DISCONNECT: () => {
			return {
				mod_id: 0,
			}
		},

		MODULE_READY: () => {
			return {
				mod_id: 0,
			}
		},

		SAVE_MESSAGE_LOG: () => {
			return {
				pathname: "",
				pathname_length: 0,
			}
		},

		TIMING_MESSAGE: () => {
			return {
				timing: Array(MAX_MESSAGE_TYPES).fill(0),
				ModulePID: Array(MAX_MODULES).fill(0),
				send_time: 0,
			}
		},

		MJVR_MSG_HEADER: () => {
			return {
				serial_no: 0,
				sub_sample: 0,
			}
		},

		MUJOCO_VR_REQUEST_STATE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
			}
		},

		MUJOCO_VR_REPLY_STATE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				requester_MID: 0,
				reserved: 0,
				sim_time: 0,
				body_position: Array(3 * MJ_VR_MAX_BODY_COUNT).fill(0),
				body_orientation: Array(4 * MJ_VR_MAX_BODY_COUNT).fill(0),
				motor_ctrltype: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				motor_position: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				motor_velocity: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				joint_position: Array(MJ_VR_MAX_JOINT_DOF).fill(0),
				joint_velocity: Array(MJ_VR_MAX_JOINT_DOF).fill(0),
				joint_torque: Array(MJ_VR_MAX_JOINT_DOF).fill(0),
				contact: Array(MJ_VR_MAX_CONTACT_COUNT).fill(0),
			}
		},

		MUJOCO_VR_REQUEST_MODEL_INFO: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
			}
		},

		MUJOCO_VR_REPLY_MODEL_INFO: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				requester_MID: 0,
				reserved: 0,
				model_file: "",
				sim_time: 0,
				nq: 0,
				nv: 0,
				num_body: 0,
				num_mocap: 0,
				num_float: 0,
				num_motor: 0,
				num_joint: 0,
				num_contact: 0,
				num_tendon: 0,
				reserved1: 0,
				body_id: Array(MJ_VR_MAX_BODY_COUNT).fill(0),
				mocap_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
				float_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
				motor_id: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				joint_id: Array(MJ_VR_MAX_JOINT_COUNT).fill(0),
				contact_id: Array(MJ_VR_MAX_CONTACT_COUNT).fill(0),
				tendon_id: Array(MJ_VR_MAX_TENDON_COUNT).fill(0),
				joint_type: Array(MJ_VR_MAX_JOINT_COUNT).fill(0),
				max_motor_limits: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				min_motor_limits: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				body_names: "",
				mocap_names: "",
				float_names: "",
				motor_names: "",
				joint_names: "",
				contact_names: "",
				tendon_names: "",
			}
		},

		MUJOCO_VR_REQUEST_LINK_STATE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
			}
		},

		MUJOCO_VR_REPLY_LINK_STATE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				requester_MID: 0,
				reserved: 0,
				nlink: 0,
				nfloat: 0,
				body_linkid: Array(MJ_VR_MAX_BODY_COUNT).fill(0),
				link_followerid: Array(MJ_VR_MAX_BODY_COUNT).fill(0),
				link_leaderid: Array(MJ_VR_MAX_BODY_COUNT).fill(0),
				link_active: "",
				link_rpos: Array(3 * MJ_VR_MAX_BODY_COUNT).fill(0),
				link_quat_leader: Array(4 * MJ_VR_MAX_BODY_COUNT).fill(0),
				link_quat_follower: Array(4 * MJ_VR_MAX_BODY_COUNT).fill(0),
			}
		},

		MUJOCO_VR_LINK: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_links: 0,
				padding: 0,
				follower_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
				leader_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
			}
		},

		MUJOCO_VR_LINK_RESET: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_links: 0,
				padding: 0,
				follower_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
			}
		},

		MUJOCO_VR_MOCAP_MOVE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_id: 0,
				padding: 0,
				id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
				position: Array(3 * MJ_VR_MAX_MOCAP_COUNT).fill(0),
				orientation: Array(4 * MJ_VR_MAX_MOCAP_COUNT).fill(0),
			}
		},

		MUJOCO_VR_MOTOR_MOVE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_id: 0,
				padding: 0,
				id: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				position: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
			}
		},

		MUJOCO_VR_FLOATBODY_MOVE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_id: 0,
				padding: 0,
				float_body_id: Array(MJ_VR_MAX_MOCAP_COUNT).fill(0),
				position: Array(3 * MJ_VR_MAX_MOCAP_COUNT).fill(0),
				orientation: Array(4 * MJ_VR_MAX_MOCAP_COUNT).fill(0),
				disable_link: "",
			}
		},

		MUJOCO_VR_LOAD_MODEL: () => {
			return {
				model_filename: "",
			}
		},

		MUJOCO_VR_SET_RGBA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				type: 0,
				id: 0,
				rgba: Array(4).fill(0),
			}
		},

		MUJOCO_VR_MOTOR_CONFIG: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_id: 0,
				padding: 0,
				id: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				type: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				k_p: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				k_i: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				k_d: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				setpt: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
			}
		},

		MUJOCO_VR_MOTOR_CTRL: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_id: 0,
				padding: 0,
				id: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				ctrl: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
			}
		},

		MUJOCO_VR_MSG: () => {
			return {
				message: "",
				position: 0,
			}
		},

		MSG_HEADER: () => {
			return {
				serial_no: 0,
				sub_sample: 0,
			}
		},

		TRIAL_METADATA: () => {
			return {
				session_num: 0,
				set_num: 0,
				block_num: 0,
				trial_num: 0,
				session_type: "",
				subject_id: "",
			}
		},

		REP_START: () => {
			return {
				rep_num: 0,
				reserved: 0,
			}
		},

		PLAYSOUND: () => {
			return {
				filename: "",
			}
		},

		PLAYVIDEO: () => {
			return {
				filename: "",
			}
		},

		START_TIMED_RECORDING: () => {
			return {
				start_command: 0,
			}
		},

		TASK_STATE_CONFIG: () => {
			return {
				state_name: "",
				target: Array(MAX_COMMAND_DIMS).fill(0),
				active_assist_weight: Array(NUM_DOMAINS).fill(0),
				brain_control_weight: Array(NUM_DOMAINS).fill(0),
				passive_assist_weight: Array(NUM_DOMAINS).fill(0),
				jstick_control_weight: Array(NUM_DOMAINS).fill(0),
				gain: Array(NUM_DOMAINS).fill(0),
				threshold: Array(NUM_DOMAINS).fill(0),
				force_targ: Array(MAX_GRIP_DIMS).fill(0),
				dZ_gain: 0,
				force_thresh: 0,
				active_override: Array(MAX_COMMAND_DIMS).fill(0),
				use_for_calib: 0,
				result_code: 0,
				stim_enable: 0,
				force_calib: 0,
				targ_set: 0,
				targ_idx: 0,
				gripperControlMask: Array(4).fill(0),
			}
		},

		PHASE_RESULT: () => {
			return {
				state_name: "",
				target: Array(MAX_COMMAND_DIMS).fill(0),
				active_assist_weight: Array(NUM_DOMAINS).fill(0),
				brain_control_weight: Array(NUM_DOMAINS).fill(0),
				passive_assist_weight: Array(NUM_DOMAINS).fill(0),
				jstick_control_weight: Array(NUM_DOMAINS).fill(0),
				gain: Array(NUM_DOMAINS).fill(0),
				threshold: Array(NUM_DOMAINS).fill(0),
				force_targ: Array(MAX_GRIP_DIMS).fill(0),
				dZ_gain: 0,
				force_thresh: 0,
				active_override: Array(MAX_COMMAND_DIMS).fill(0),
				use_for_calib: 0,
				result_code: 0,
				stim_enable: 0,
				force_calib: 0,
				targ_set: 0,
				targ_idx: 0,
				gripperControlMask: Array(4).fill(0),
			}
		},

		EXEC_SCORE: () => {
			return {
				passed: 0,
				failed: 0,
			}
		},

		FLIP_THAT_BUCKET_DATA: () => {
			return {
				state_name: "",
				state_value: 0,
			}
		},

		PICDISPLAY: () => {
			return {
				filename: "",
				timer: 0,
			}
		},

		STIMDATA: () => {
			return {
				ConfigID: Array(12).fill(0),
				Vmax: Array(12).fill(0),
				Vmin: Array(12).fill(0),
				interphase: Array(12).fill(0),
			}
		},

		TDMS_CREATE: () => {
			return {
				pathname: "",
				pathname_length: 0,
				reserved: 0,
			}
		},

		STIM_VOLTAGE_MONITOR_DATA: () => {
			return {
				sample_rate: 0,
				pulse_count: 0,
				daq_channel: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
				array_channel: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
				daq_timestamp: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
				voltage: Array(NUM_SPIKES_PER_STIM_MSG * 100).fill(0),
				interphase: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
				Vmax: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
				Vmin: Array(NUM_SPIKES_PER_STIM_MSG).fill(0),
			}
		},

		STIM_VOLTAGE_MONITOR_DIGITAL_DATA: () => {
			return {
				stim_sync_event: Array(30).fill(0),
				stim_param_event: Array(5).fill(0),
				spm_daq_delta_t: 0,
			}
		},

		VOLTAGE_MONITOR_STATUS: () => {
			return {
				msg_length: 0,
				msg: "",
			}
		},

		STIM_DUTYCYCLE_TIME: () => {
			return {
				dutycycle_time: 0,
			}
		},

		STIM_TRIAL_DURATION: () => {
			return {
				trial_duration: 0,
			}
		},

		ATIforcesensor: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				Fx: 0,
				Fy: 0,
				Fz: 0,
				Tz: 0,
				Tx: 0,
				Ty: 0,
			}
		},

		SEAIO_OUT: () => {
			return {
				bit: 0,
				value: 0,
			}
		},

		HSTLOG: () => {
			return {
				len: 0,
				reserved: 0,
				log: "",
			}
		},

		EM_CONFIGURATION: () => {
			return {
				type: 0,
				reserved: 0,
				data: "",
			}
		},

		EXTRACTION_RESPONSE: () => {
			return {
				src: 0,
				decoder_type: "",
				decoder_loc: "",
			}
		},

		UPDATE_UNIT_STATE: () => {
			return {
				unit_idx: 0,
				enabled: 0,
			}
		},

		DISABLED_UNITS: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				disabled_units: Array(MAX_TOTAL_SPIKE_CHANS).fill(0),
			}
		},

		CONTROL_SPACE_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				command: Array(MAX_COMMAND_DIMS).fill(0),
				dZ: Array(MAX_GRIP_DIMS).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		BIAS_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				command: Array(MAX_COMMAND_DIMS).fill(0),
				dZ: Array(MAX_GRIP_DIMS).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		IMPEDANCE_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stiffness: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		CONTROL_SPACE_POS_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				command: Array(MAX_COMMAND_DIMS).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		FINISHED_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				command: Array(MAX_COMMAND_DIMS).fill(0),
				stiffness: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		EXECUTIVE_CTRL: () => {
			return {
				proceed: 0,
				fail: 0,
				reserved: 0,
			}
		},

		CONTROL_SPACE_FEEDBACK: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				position: Array(MAX_COMMAND_DIMS).fill(0),
				velocity: Array(MAX_COMMAND_DIMS).fill(0),
			}
		},

		MPL_RAW_PERCEPT: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				position: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				velocity: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				torque: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				temperature: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
			}
		},

		MPL_SEGMENT_PERCEPTS: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				ind_force: Array(14).fill(0),
				mid_force: Array(14).fill(0),
				rng_force: Array(14).fill(0),
				lit_force: Array(14).fill(0),
				thb_force: Array(14).fill(0),
				ind_accel: Array(3).fill(0),
				mid_accel: Array(3).fill(0),
				rng_accel: Array(3).fill(0),
				lit_accel: Array(3).fill(0),
				thb_accel: Array(3).fill(0),
				contacts: Array(16).fill(0),
			}
		},

		MPL_REBIASED_SENSORDATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				torque: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				ind_force: Array(14).fill(0),
				mid_force: Array(14).fill(0),
				rng_force: Array(14).fill(0),
				lit_force: Array(14).fill(0),
				thb_force: Array(14).fill(0),
				contacts: Array(16).fill(0),
			}
		},

		CURSOR_FEEDBACK: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				torque: Array(MPL_RAW_PERCEPT_DIMS).fill(0),
				ind_force: Array(14).fill(0),
				mid_force: Array(14).fill(0),
				rng_force: Array(14).fill(0),
				lit_force: Array(14).fill(0),
				thb_force: Array(14).fill(0),
				contacts: Array(16).fill(0),
			}
		},

		VISUAL_GRATING_BUILD: () => {
			return {
				grating_visibility: 0,
				stimulation_on: 0,
				trial_set: 0,
				presentation: 0,
				increment_block: 0,
				wait_response: 0,
				reserved: 0,
			}
		},

		VISUAL_GRATING_RESPONSE: () => {
			return {
				channel: 0,
				session_num: 0,
				set_num: 0,
				block_num: 0,
				trial_num: 0,
				block_ID: 0,
				DELTA_reference_frequency: 0,
				ICMS_reference_frequency: 0,
				ICMS_reference_amplitude: 0,
				ICMS_frequency_1: 0,
				ICMS_frequency_2: 0,
				ICMS_amplitude_1: 0,
				ICMS_amplitude_2: 0,
				VIS_reference_frequency: 0,
				VIS_reference_amplitude: 0,
				VIS_frequency_1: 0,
				VIS_frequency_2: 0,
				VIS_amplitude_1: 0,
				VIS_amplitude_2: 0,
				response: 0,
			}
		},

		WAM_FEEDBACK: () => {
			return {
				position: Array(7).fill(0),
				velocity: Array(7).fill(0),
			}
		},

		RAW_CTSDATA: () => {
			return {
				source_index: 0,
				num_chans_enabled: 0,
				source_timestamp: 0,
				data: Array(LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_CHANS_PER_SOURCE).fill(0),
			}
		},

		RAW_CTSDATA_N256: () => {
			return {
				source_index: 0,
				num_chans_enabled: 0,
				source_timestamp: 0,
				data: Array(LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_CHANS_PER_SOURCE_N256).fill(0),
			}
		},

		RAW_ANALOGDATA: () => {
			return {
				source_index: 0,
				num_chans_enabled: 0,
				source_timestamp: 0,
				data: Array(ANALOGSAMPLES_PER_HEARTBEAT * MAX_ANALOG_CHANS).fill(0),
			}
		},

		SPM_CTSDATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: Array(MAX_SPIKE_SOURCES).fill(0),
				data: Array(RAW_COUNTS_PER_SAMPLE * LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_SOURCES * MAX_SPIKE_CHANS_PER_SOURCE).fill(0),
			}
		},

		SPM_ANALOGDATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: Array(MAX_SPIKE_SOURCES).fill(0),
				data: Array(RAW_COUNTS_PER_SAMPLE * LFPSAMPLES_PER_HEARTBEAT * MAX_SPIKE_SOURCES * MAX_ANALOG_CHANS).fill(0),
			}
		},

		RAW_SPIKECOUNT: () => {
			return {
				source_index: 0,
				reserved: 0,
				source_timestamp: 0,
				count_interval: 0,
				counts: Array(MAX_TOTAL_SPIKE_CHANS_PER_SOURCE).fill(0),
			}
		},

		RAW_SPIKECOUNT_N256: () => {
			return {
				source_index: 0,
				reserved: 0,
				source_timestamp: 0,
				count_interval: 0,
				counts: Array(MAX_TOTAL_SPIKE_CHANS_PER_SOURCE_N256).fill(0),
			}
		},

		SPM_SPIKECOUNT: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: Array(MAX_SPIKE_SOURCES).fill(0),
				count_interval: 0,
				counts: Array(MAX_TOTAL_SPIKE_CHANS).fill(0),
			}
		},

		SPIKE_SNIPPET: () => {
			return {
				source_index: 0,
				channel: 0,
				unit: 0,
				reserved1: 0,
				source_timestamp: 0,
				fPattern: Array(3).fill(0),
				nPeak: 0,
				nValley: 0,
				reserved2: 0,
				snippet: Array(SAMPLES_PER_SNIPPET).fill(0),
			}
		},

		SPIKE_SNIPPET: () => {
			return {
				ss: {
					source_index: 0,
					channel: 0,
					unit: 0,
					reserved1: 0,
					source_timestamp: 0,
					fPattern: Array(3).fill(0),
					nPeak: 0,
					nValley: 0,
					reserved2: 0,
					snippet: Array(SAMPLES_PER_SNIPPET).fill(0),
				},
			}
		},

		REJECTED_SNIPPET: () => {
			return {
				source_index: 0,
				channel: 0,
				unit: 0,
				reserved1: 0,
				source_timestamp: 0,
				fPattern: Array(3).fill(0),
				nPeak: 0,
				nValley: 0,
				rejectType: 0,
				snippet: Array(SAMPLES_PER_SNIPPET).fill(0),
			}
		},

		REJECTED_SNIPPET: () => {
			return {
				rs: {
					source_index: 0,
					channel: 0,
					unit: 0,
					reserved1: 0,
					source_timestamp: 0,
					fPattern: Array(3).fill(0),
					nPeak: 0,
					nValley: 0,
					rejectType: 0,
					snippet: Array(SAMPLES_PER_SNIPPET).fill(0),
				},
			}
		},

		RAW_DIGITAL_EVENT: () => {
			return {
				source_index: 0,
				channel: 0,
				source_timestamp: 0,
				data: Array(2).fill(0),
			}
		},

		SPM_DIGITAL_EVENT: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_index: Array(MAX_DIG_PER_SAMPLE).fill(0),
				source_timestamp: Array(MAX_SPIKE_SOURCES).fill(0),
				byte0: Array(MAX_DIG_PER_SAMPLE).fill(0),
				byte1: Array(MAX_DIG_PER_SAMPLE).fill(0),
				num_events: 0,
				reserved: 0,
			}
		},

		STIM_SYNC_EVENT: () => {
			return {
				source_index: 0,
				channel: 0,
				source_timestamp: 0,
				data: 0,
				reserved: 0,
			}
		},

		STIM_UPDATE_EVENT: () => {
			return {
				source_index: 0,
				channel: 0,
				source_timestamp: 0,
				data: 0,
				reserved: 0,
			}
		},

		CENTRALRECORD: () => {
			return {
				pathname: "",
				subjectID: "",
				record: 0,
				reserved: 0,
			}
		},

		INPUT_DOF_DATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				tag: "",
				dof_vals: Array(MAX_COMMAND_DIMS).fill(0),
			}
		},

		DATAGLOVE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				tag: "",
				raw_vals: Array(MAX_DATAGLOVE_SENSORS).fill(0),
				calib_vals: Array(MAX_DATAGLOVE_SENSORS).fill(0),
				gesture: 0,
				glovetype: 0,
				hand: 0,
				reserved: 0,
			}
		},

		SLIDER_DATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				type: 0,
				channel: 0,
				value: 0,
				time: 0,
			}
		},

		USER_DEFINED_STIM: () => {
			return {
				frequency: 0,
				amplitude: Array(3).fill(0),
				channel: Array(3).fill(0),
			}
		},

		USER_BEHAVIOUR: () => {
			return {
				current_trial: 0,
				current_screen: "",
				current_object: "",
				left_canvas: Array(2).fill(0),
				right_canvas: Array(2).fill(0),
				frequency: 0,
				freq_choice: 0,
				bio: 0,
				drag: 0,
				amplitude: Array(3).fill(0),
				satisfaction: 0,
				certainty: 0,
				chosen_object: "",
				object_quest: Array(6).fill(0),
				affective_quest: Array(5).fill(0),
			}
		},

		STOP_STIM: () => {
			return {
				stop_stim: 0,
			}
		},

		PAUSE_TRIAL: () => {
			return {
				pause_trial: 0,
			}
		},

		CERESTIM_CONFIG_MODULE: () => {
			return {
				configID: Array(MAX_CS_CONFIGS).fill(0),
				amp1: Array(MAX_CS_CONFIGS).fill(0),
				amp2: Array(MAX_CS_CONFIGS).fill(0),
				frequency: Array(MAX_CS_CONFIGS).fill(0),
				num_modules: 0,
				afcf: 0,
				width1: 0,
				width2: 0,
				interphase: 0,
			}
		},

		CERESTIM_CONFIG_CHAN: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stop: 0,
				numChans: 0,
				channel: Array(MAX_STIM_CHANS_ON).fill(0),
				pattern: Array(MAX_STIM_CHANS_ON).fill(0),
				reps: 0,
				pause_t: 0,
			}
		},

		CERESTIM_CONFIG_CHAN_ARBITRARY: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stop: 0,
				pathname: "",
				pathlength: 0,
				pulselength: 0,
			}
		},

		CERESTIM_CONFIG_CHAN_PRESAFETY: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stop: 0,
				numChans: 0,
				channel: Array(NUM_STIM_CHANS).fill(0),
				pattern: Array(NUM_STIM_CHANS).fill(0),
				reps: 0,
				pause_t: 0,
			}
		},

		CERESTIM_CONFIG_CHAN_PRESAFETY_ARBITRARY: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stop: 0,
				numChans: 0,
				channel: Array(NUM_STIM_CHANS).fill(0),
				pattern: Array(NUM_STIM_CHANS).fill(0),
				reps: 0,
				reserved: 0,
				pathname: "",
				pathlength: 0,
			}
		},

		CERESTIM_ERROR: () => {
			return {
				error: 0,
				config: 0,
			}
		},

		RF_REPORT: () => {
			return {
				handp: "",
				handd: "",
				head: "",
				arms: "",
				tag: 0,
				flipframe: 0,
			}
		},

		AJA_CONFIG: () => {
			return {
				record: 0,
				stop: 0,
				filename: "",
			}
		},

		AJA_TIMECODE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				timecode: "",
			}
		},

		AJA_STATUS: () => {
			return {
				status: 0,
				reserved: 0,
				clipname: "",
			}
		},

		NORMALIZATION_FACTOR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				factor: 0,
				length: 0,
			}
		},

		CST_LAMBDA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				lambda: 0,
				k: 0,
				cursor_pos: 0,
			}
		},

		CST_SETTINGS: () => {
			return {
				sweep_rate: 0,
				vis_bins: 0,
				stim_bins: 0,
			}
		},

		NATURAL_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		DEPTH_RESPONSE: () => {
			return {
				idx: 0,
				reserved: 0,
			}
		},

		PAIN_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		MODALITY_TOGGLE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		MECH_RESPONSE: () => {
			return {
				idx: 0,
				reserved: 0,
			}
		},

		MECH_INTENSITY_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		MOVE_INTENSITY_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		TINGLE_INTENSITY_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		MOVE_RESPONSE: () => {
			return {
				idx: 0,
				reserved: 0,
			}
		},

		DIR_PIXEL_COORDS: () => {
			return {
				img: "",
				moreMsgs: 0,
				reserved: 0,
				pixels: Array(64).fill(0),
			}
		},

		TINGLE_RESPONSE: () => {
			return {
				idx: 0,
				reserved: 0,
			}
		},

		TEMP_RESPONSE: () => {
			return {
				a: 0,
				reserved: 0,
			}
		},

		PIXEL_COORDS: () => {
			return {
				img: "",
				moreMsgs: 0,
				reserved: 0,
				pixels: Array(64).fill(0),
			}
		},

		STIM_PRES_CONFIG: () => {
			return {
				filename: "",
				randomization: 0,
			}
		},

		STIM_PRESENT: () => {
			return {
				stim_filename: "",
				stim_state_name: "",
				stim_display_time: 0,
				stim_start_delay: 0,
			}
		},

		STIM_PRES_PHASE_END: () => {
			return {
				phase_rep_end: 0,
			}
		},

		STIM_PRES_STATUS: () => {
			return {
				pause_resume: 0,
				stop: 0,
			}
		},

		STIM_CONFIG_TYPE: () => {
			return {
				stim_configtype: "",
			}
		},

		GRIP_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				grip_pos: Array(MAX_GRIPPER_DIMS).fill(0),
				velocity: Array(MAX_GRIPPER_DIMS).fill(0),
				force: Array(MAX_GRIPPER_DIMS).fill(0),
				impedance: Array(MAX_GRIPPER_DIMS).fill(0),
				controlMask: Array(4).fill(0),
				src: 0,
				reserved: 0,
			}
		},

		GRIP_FINISHED_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				grip_pos: Array(MAX_GRIPPER_DIMS).fill(0),
				velocity: Array(MAX_GRIPPER_DIMS).fill(0),
				force: Array(MAX_GRIPPER_DIMS).fill(0),
				impedance: Array(MAX_GRIPPER_DIMS).fill(0),
				controlMask: Array(4).fill(0),
				effector: "",
			}
		},

		GRIPPER_FEEDBACK: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				grip_pos: Array(MAX_GRIPPER_DIMS).fill(0),
				velocity: Array(MAX_GRIPPER_DIMS).fill(0),
				force: Array(MAX_GRIPPER_FORCES).fill(0),
				effector: "",
			}
		},

		MUJOCO_SENSOR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				motor_pos: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				motor_vel: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				motor_torque: Array(MJ_VR_MAX_MOTOR_COUNT).fill(0),
				joint_pos: Array(MJ_VR_MAX_JOINT_COUNT).fill(0),
				joint_vel: Array(MJ_VR_MAX_JOINT_COUNT).fill(0),
				contact: Array(MJ_VR_MAX_CONTACT_COUNT).fill(0),
			}
		},

		MUJOCO_CMD: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				ref_pos: Array(MJ_MAX_MOTOR).fill(0),
				ref_vel: Array(MJ_MAX_MOTOR).fill(0),
				gain_pos: Array(MJ_MAX_MOTOR).fill(0),
				gain_vel: Array(MJ_MAX_MOTOR).fill(0),
				ref_pos_enabled: 0,
				ref_vel_enabled: 0,
				gain_pos_enabled: 0,
				gain_vel_enabled: 0,
			}
		},

		MUJOCO_MOVE: () => {
			return {
				mocap_id: 0,
				link_objects: 0,
				pos: Array(3).fill(0),
			}
		},

		MUJOCO_OBJMOVE: () => {
			return {
				obj_id: 0,
				pos: Array(3).fill(0),
				orientation: Array(3).fill(0),
			}
		},

		MUJOCO_MSG: () => {
			return {
				message: "",
				position: 0,
			}
		},

		MUJOCO_GHOST_COLOR: () => {
			return {
				color_id: 0,
			}
		},

		OPENHAND_CMD: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				motor_sp: Array(2).fill(0),
				reserved1: Array(2).fill(0),
				mode: 0,
				reserved2: Array(3).fill(0),
			}
		},

		OPENHAND_SENS: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				motor_pos: 0,
				force: 0,
			}
		},

		OPTITRACK_RIGID_BODY: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				ID: 0,
				reserved: 0,
				pos: Array(3).fill(0),
				orient: Array(3).fill(0),
				timestamp: 0,
				name: "",
			}
		},

		SINGLETACT_DATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				raw_analog: Array(3).fill(0),
				force: Array(3).fill(0),
			}
		},

		DEKA_CAN_MSG: () => {
			return {
				can_id: 0,
				data: Array(8).fill(0),
				padding: 0,
			}
		},

		DEKA_ACI_RESPONSE: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				ACI_1: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				ACI_2: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				ACI_3: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
			}
		},

		DEKA_SENSOR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				position_msg_1: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				position_msg_2: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				motor_pos: Array(DEKA_DOF_COUNT).fill(0),
				motor_current: Array(DEKA_DOF_COUNT).fill(0),
				mode: 0,
				sync: 0,
				grip: 0,
				padding: 0,
			}
		},

		DEKA_CAN_TOGGLE: () => {
			return {
				toggle: 0,
				padding: 0,
			}
		},

		DEKA_CAN_GRIP_TOGGLE: () => {
			return {
				toggle: 0,
				padding: 0,
			}
		},

		DEKA_CAN_EXIT: () => {
			return {
				exit: 0,
				padding: 0,
			}
		},

		KUKA_JOINT_COMMAND: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				joint_dest: Array(KUKA_DOF_COUNT).fill(0),
				err_move_mode: 0,
				err_input_cap: Array(6).fill(0),
				err_cart_wall_eef: Array(6).fill(0),
				err_cart_wall_arm: Array(6).fill(0),
				err_jpos_stop: Array(3).fill(0),
			}
		},

		KUKA_FEEDBACK: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				time: 0,
				joint_pos: Array(KUKA_DOF_COUNT).fill(0),
				cart_pos: Array(3).fill(0),
				cart_angle: Array(3).fill(0),
				cart_pos_vel: Array(3).fill(0),
				cart_rot_vel: Array(3).fill(0),
				cart_force: Array(3).fill(0),
				cart_torque: Array(3).fill(0),
				dest_delta_t: 0,
				mode: 0,
				reserved: 0,
			}
		},

		KUKA_EXIT: () => {
			return {
				exit: 0,
				padding: 0,
			}
		},

		KUKA_PTP_JOINT: () => {
			return {
				joint_pos: Array(KUKA_DOF_COUNT).fill(0),
			}
		},

		KUKA_DEBUG: () => {
			return {
				joint_pos: Array(KUKA_DOF_COUNT).fill(0),
			}
		},

		XIPP_EMG_DATA_RAW: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				num_chans_per_headstage: Array(MAX_XIPP_EEG_HEADSTAGES).fill(0),
				source_timestamp: Array(XIPP_SAMPLES_PER_MSG).fill(0),
				data: Array(XIPP_SAMPLES_PER_MSG * MAX_XIPP_CHANS).fill(0),
			}
		},

		MYO_EMG_DATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: Array(MYO_SAMPLES_PER_MSG).fill(0),
				data: Array(MYO_SAMPLES_PER_MSG * MAX_MYO_EMG_CHANS).fill(0),
			}
		},

		MYO_KIN_DATA: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: 0,
				orientation: Array(4).fill(0),
				gyroscope: Array(3).fill(0),
				acceleration: Array(3).fill(0),
			}
		},

		SAMPLE_GENERATED: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				source_timestamp: 0,
				xipp_timestamp: 0,
				reserved: 0,
			}
		},

		PRENSILIA_SENS: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				stream_type: 0,
				current: Array(PRENSILIA_DOF).fill(0),
				position: Array(PRENSILIA_DOF).fill(0),
				external: Array(PRENSILIA_EXT_SENSORS).fill(0),
				tension: Array(PRENSILIA_DOF).fill(0),
				reserved: 0,
			}
		},

		PRENSILIA_CMD: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				mode: Array(PRENSILIA_DOF).fill(0),
				command: Array(PRENSILIA_DOF).fill(0),
			}
		},

		DEKA_HAND_SENSOR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				position_msg_1: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				position_msg_2: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				force_msg_1: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				force_msg_2: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				force_msg_3: {
					can_id: 0,
					data: Array(8).fill(0),
					padding: 0,
				},
				motor_pos: Array(HX_LUKE_MOTOR_COUNT).fill(0),
				contact: Array(HX_DEKA_LUKE_CONTACT_COUNT).fill(0),
				mode: 0,
				status: Array(HX_DEKA_LUKE_CONTACT_COUNT).fill(0),
				sync: 0,
				grip: 0,
			}
		},

		DEKA_HAND_JSTICK_CMD: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				ref_vel: Array(HX_LUKE_MOTOR_COUNT).fill(0),
			}
		},

		RH_FINGER_DATA: () => {
			return {
				proximal_angle: 0,
				distal_angle: 0,
				pressure: Array(NUM_SENSORS_PER_FINGER).fill(0),
				contact: Array(NUM_SENSORS_PER_FINGER).fill(0),
			}
		},

		DYNAMIXEL_INFO: () => {
			return {
				joint_angle: Array(NUM_DYNAMIXEL).fill(0),
				raw_angle: Array(NUM_DYNAMIXEL).fill(0),
				velocity: Array(NUM_DYNAMIXEL).fill(0),
				load: Array(NUM_DYNAMIXEL).fill(0),
				voltage: Array(NUM_DYNAMIXEL).fill(0),
				temperature: Array(NUM_DYNAMIXEL).fill(0),
			}
		},

		RH_GRIPPER_SENSOR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				finger_1: {
					proximal_angle: 0,
					distal_angle: 0,
					pressure: Array(NUM_SENSORS_PER_FINGER).fill(0),
					contact: Array(NUM_SENSORS_PER_FINGER).fill(0),
				},
				finger_2: {
					proximal_angle: 0,
					distal_angle: 0,
					pressure: Array(NUM_SENSORS_PER_FINGER).fill(0),
					contact: Array(NUM_SENSORS_PER_FINGER).fill(0),
				},
				finger_3: {
					proximal_angle: 0,
					distal_angle: 0,
					pressure: Array(NUM_SENSORS_PER_FINGER).fill(0),
					contact: Array(NUM_SENSORS_PER_FINGER).fill(0),
				},
				motor_info: {
					joint_angle: Array(NUM_DYNAMIXEL).fill(0),
					raw_angle: Array(NUM_DYNAMIXEL).fill(0),
					velocity: Array(NUM_DYNAMIXEL).fill(0),
					load: Array(NUM_DYNAMIXEL).fill(0),
					voltage: Array(NUM_DYNAMIXEL).fill(0),
					temperature: Array(NUM_DYNAMIXEL).fill(0),
				},
			}
		},

		TABLE_LOAD_CELLS: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				left_plate: Array(4).fill(0),
				left_plate_mean: 0,
				center_plate: Array(4).fill(0),
				center_plate_mean: 0,
				right_plate: Array(4).fill(0),
				right_plate_mean: 0,
			}
		},

		TASKA_CMD: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				op_code: 0,
				padding: Array(7).fill(0),
				stx: 0,
				type: 0,
				sub_index: 0,
				length: 0,
				data: Array(60).fill(0),
			}
		},

		TASKA_REPLY: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				tx_timestamp: 0,
				rx_timestamp: 0,
				comm_time: 0,
				op_code: 0,
				padding: Array(7).fill(0),
				stx: 0,
				type: 0,
				sub_index: 0,
				length: 0,
				data: Array(60).fill(0),
			}
		},

		TASKA_ERROR: () => {
			return {
				header: {
					serial_no: 0,
					sub_sample: 0,
				},
				error_code: 0,
				reserved: 0,
				msg: "",
				dump: Array(64).fill(0),
			}
		},

		MECH_STIM_CONFIGURE: () => {
			return {
				source: 0,
				length: 0,
				str: "",
			}
		},

		EXIT: () => {
			return {
			}
		},

		KILL: () => {
			return {
			}
		},

		ACKNOWLEDGE: () => {
			return {
			}
		},

		DISCONNECT: () => {
			return {
			}
		},

		FORCED_DISCONNECT: () => {
			return {
			}
		},

		MUJOCO_VR_RESET: () => {
			return {
			}
		},

		MUJOCO_VR_RELOAD: () => {
			return {
			}
		},

		MUJOCO_VR_PAUSE: () => {
			return {
			}
		},

		MUJOCO_VR_RESUME: () => {
			return {
			}
		},

		CONTROL_SPACE_FEEDBACK_RHR_GRIPPER: () => {
			return {
			}
		},

		REZERO_GRIPPER_SENSORS: () => {
			return {
			}
		},

		EXTRACTION_REQUEST: () => {
			return {
			}
		},

		TRIAL_END: () => {
			return {
			}
		},

		REP_END: () => {
			return {
			}
		},

		EM_ADAPT_NOW: () => {
			return {
			}
		},

		TACTOR_CMD: () => {
			return {
			}
		},

		AJA_STATUS_REQUEST: () => {
			return {
			}
		},

		CERESTIM_ALIVE: () => {
			return {
			}
		},

		CS_TRAIN_END: () => {
			return {
			}
		},

		CS_ARBITRARY_CLOSE: () => {
			return {
			}
		},

		CLEAR_LINE: () => {
			return {
			}
		},

		ADD_SENSATION: () => {
			return {
			}
		},

		MECH_STIM_RESET: () => {
			return {
			}
		},

		MECH_STIM_STAGE: () => {
			return {
			}
		},

		MECH_STIM_WAITING: () => {
			return {
			}
		},

		MECH_STIM_TRIGGER: () => {
			return {
			}
		},

		MECH_STIM_CANCEL: () => {
			return {
			}
		},

		MECH_STIM_DONE: () => {
			return {
			}
		},

		MECH_STIM_ERROR: () => {
			return {
			}
		},

	},
};
