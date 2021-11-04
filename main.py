#!/usr/bin/env python3

from twisted.internet import reactor

from HL7Server.HL7Server import HL7ServerFactory, HL7ServerLoggingReceiver
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

    def main(self):
        """

        :return:
        """
        self.logger.info('Application {} started'.format(APL_NAME))

        try:

            reactor.listenTCP(self.user_cfg.server_port.value, HL7ServerFactory(HL7ServerLoggingReceiver()))
            reactor.run()
        except BaseException as exc:
            self.logger.error(exc)

        self.logger.info('Application {} stopped'.format(APL_NAME))


if __name__ == '__main__':
    logger_init(APL_NAME)
    Main().main()
