# /usr/bin/python
# encoding:utf-8
import logging


class YwfLog:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    @staticmethod
    def fatal(message, *args, **kwargs):
        logging.critical(message, *args, **kwargs)

    @staticmethod
    def error(message, *args, **kwargs):
        logging.error(message, *args, **kwargs)

    @staticmethod
    def warning(message, *args, **kwargs):
        logging.warning(message, *args, **kwargs)

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def debug(message):
        logging.debug(message)
