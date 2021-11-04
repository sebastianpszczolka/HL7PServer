import configparser

from lib.core.log import LogMixin


class ConfParam(object):
    def __init__(self, group_name=None, key=None, value=None, def_val=None, type_val=str):
        self.group_name = group_name
        self.key = key
        self.value = value
        self.default_value = def_val
        self.type_val = type_val
        if self.value is None:
            self.value = def_val


# noinspection PyBroadException
class Conf(LogMixin):
    def __init__(self, filename):
        self.filename = filename
        self.cfg_array = []

    def read_configuration(self):
        ret_status = True

        self.logger.info('ConfigurationFileIs: {}'.format(self.filename))
        try:
            self.logger.info('ReadCfgStart')
            config = configparser.RawConfigParser()

            if config.read(self.filename):
                self.logger.info('Opened Cfg file')

                for item in self.cfg_array:
                    item.value = item.type_val(config.get(item.group_name, item.key))
                    self.logger.info('CFG->: {}={}'.format(item.key, item.value))
            else:
                self.logger.error('Error in opening Cfg file.')
                ret_status = False

        except BaseException:
            ret_status = False
            self.logger.exception('ReadingConfiguration')

        self.logger.info('ReadCfgStop')
        return ret_status

    def write_configuration(self, set_default=False):

        ret_status = True

        self.logger.info('ConfigurationFileIs: {}'.format(self.filename))
        try:
            self.logger.info('WriteCfgStart')
            config = configparser.RawConfigParser()
            if not set_default:
                if config.read(self.filename):
                    self.logger.info('Opened Cfg file')

                    for item in self.cfg_array:
                        config.set(item.group_name, item.key, item.value)

                else:
                    self.logger.error('Opened Cfg file')
                    ret_status = False
            else:
                self.logger.info('Restoring to Default Cfg file')

                for item in self.cfg_array:
                    try:
                        config.add_section(item.group_name)
                    except configparser.DuplicateSectionError:
                        pass

                    config.set(item.group_name, item.key, item.default_value)

            with open(self.filename, "w") as config_file:
                config.write(config_file)

        except BaseException:
            ret_status = False
            self.logger.exception('WritingConfiguration')

        self.logger.info('WriteCfgStop')
        self.read_configuration()
        return ret_status
