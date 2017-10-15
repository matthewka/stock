from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

CONFIG_SEC_LOG_LEVEL = "log_level"

CONFIG_OPT_LOG_DEBUG = "log_level_debug"
CONFIG_OPT_LOG_VERBOSE = "log_level_verbose"

DEBUG = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_DEBUG)
VERBOSE = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_VERBOSE)