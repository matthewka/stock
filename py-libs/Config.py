from configparser import ConfigParser

class Config:
    def __init__(self):
        cfg = ConfigParser()
        cfg.read('config.ini')
        # with open("config.ini") as f:
        #     config_file = f.read()
        #
        # config = configparser.RawConfigParser(allow_no_value=True)
        # config.read(io.BytesIO(config_file))
        self.parseConfig(cfg)

    def parseConfig(self, cfg):

        global DEBUG
        global VERBOSE

        CONFIG_SEC_LOG_LEVEL = "log_level"

        CONFIG_OPT_LOG_DEBUG = "log_level_debug"
        CONFIG_OPT_LOG_VERBOSE = "log_level_verbose"
        DEBUG = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_DEBUG)
        VERBOSE = cfg.getboolean(CONFIG_SEC_LOG_LEVEL, CONFIG_OPT_LOG_VERBOSE)