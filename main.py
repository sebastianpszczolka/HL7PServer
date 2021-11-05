#!/usr/bin/env python3

from twisted.internet import reactor
from twisted.python import log
from HL7Server.HL7Server import HL7ServerFactory, HL7ServerLoggingReceiver
from database.DB import DB
from lib.core.log import LogMixin
from lib.core.log import logger_init
from AppConf import AppConf
from AppConstant import APL_NAME, VER


class Main(LogMixin):

    def __init__(self):
        """

        """

        self.logger.info('Application {}{} starting'.format(APL_NAME, VER))

        self.user_cfg = AppConf('{}.cfg'.format(APL_NAME))

        if not self.user_cfg.read_configuration():
            self.user_cfg.write_configuration(True)

        self.manage_db = DB(self.user_cfg.db_host.value, self.user_cfg.db_name.value,
                            self.user_cfg.db_user.value, self.user_cfg.db_passwd.value, self.user_cfg.db_port.value)

    def main(self):
        """

        :return:
        """
        self.logger.info('Application {} started'.format(APL_NAME))

        try:
            observer = log.PythonLoggingObserver('default')
            observer.start()

            reactor.listenTCP(self.user_cfg.server_port.value,
                              HL7ServerFactory(HL7ServerLoggingReceiver(self.manage_db)))
            reactor.run()
        except BaseException as exc:
            self.logger.error(exc)

        self.logger.info('Application {} stopped'.format(APL_NAME))


if __name__ == '__main__':
    logger_init(APL_NAME)
    Main().main()
