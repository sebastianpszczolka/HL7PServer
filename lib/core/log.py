import logging.handlers
import sys


def logger_init(file_name, logger_name='default'):
    """
    initialize logger in future we can add more parameters to library


    :param str logger_name:
    :param str file_name:
    :return:
    """
    try:

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s]{%(filename)s:%(lineno)d} ->%(levelname)s - %(message)s')

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        fh = logging.handlers.RotatingFileHandler(file_name + '.log', maxBytes=(3 * 1048576), backupCount=10,
                                                  encoding='utf-8')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    except BaseException as exc:
        print('[ERROR]-CreationLogger: {}'.format(exc))


class LogMixin:
    @property
    def logger(self):
        return logging.getLogger('default')
