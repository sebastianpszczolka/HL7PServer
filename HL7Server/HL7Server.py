import logging

from txHL7.receiver import AbstractHL7Receiver, MessageContainer
from twisted.internet import defer
from lib.core.log import LogMixin
from txHL7.mllp import IHL7Receiver, MLLPFactory


class HL7ServerLoggingReceiver(AbstractHL7Receiver, LogMixin):
    """Simple MLLP receiver implementation that logs and ACKs messages."""

    def handleMessage(self, message_container: MessageContainer):
        self.logger.info(message_container.raw_message)
        return defer.succeed(message_container.ack())


class HL7ServerFactory(MLLPFactory, LogMixin):

    def __init__(self, receiver):
        super().__init__(receiver)
        self.logger.info("HL7Server Started")
