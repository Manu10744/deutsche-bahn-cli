import logging


def get_logger(module_name):
    """
    Returns a basic logger for the given module name.

    :param module_name: the name of the module that the logger will be configured to.
    :type module_name: str

    :return: a logger configured to level `logging.INFO` for the given module.
    :rtype: logging.Logger
    """
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s >>> %(message)s')
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
