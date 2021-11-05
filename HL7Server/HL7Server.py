import logging

from txHL7.receiver import AbstractHL7Receiver, MessageContainer

from database.DB import DB
from lib.core.log import LogMixin
from txHL7.mllp import IHL7Receiver, MLLPFactory
from txHL7.receiver import AbstractHL7Receiver
from twisted.internet import threads


class HL7ServerLoggingReceiver(AbstractHL7Receiver, LogMixin):

    def __init__(self, manage_db: DB):
        self._manage_db = manage_db

    def saveMessage(self, message: MessageContainer):

        try:
            self._manage_db.save_simple_text_record(message.raw_message)
            return message.ack()
        except:
            self.logger.exception('HL7ServerLoggingReceiver->saveMessage')
            return message.ack(ack_code='AR')

    def handleMessage(self, message):
        return threads.deferToThread(self.saveMessage, message)

    def getCodec(self):
        return 'cp1250'


class HL7ServerFactory(MLLPFactory, LogMixin):

    def __init__(self, receiver):
        super().__init__(receiver)
        self.logger.info("HL7Server Started")
