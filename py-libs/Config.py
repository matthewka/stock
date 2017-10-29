from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

CONFIG_SEC_LOG_LEVEL = "log_level"

CONFIG_OPT_LOG_DEBUG = "log_level_debug"
CONFIG_OPT_LOG_VERBOSE = "log_level_verbose"

CONFIG_SEC = "config"
CONFIG_OPT_DEVELOP = "config_develop"

CONFIG_DATABASE = "database"
CONFIG_DATABASE_VERSION = "database_version"
CONFIG_DATABASE_RECORD_SIZE = "record_size"

DEBUG = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_DEBUG)
VERBOSE = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_VERBOSE)

DEVELOP = cfg.getboolean(CONFIG_SEC, CONFIG_OPT_DEVELOP)

DB_VERSION = cfg.get(CONFIG_DATABASE, CONFIG_DATABASE_VERSION)
DB_RECORD_SIZE = cfg.getint(CONFIG_DATABASE, CONFIG_DATABASE_RECORD_SIZE)