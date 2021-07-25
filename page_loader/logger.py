import logging


log_format = ('%(message)s')


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter(log_format))
    logger.addHandler(ch)
    return logger
