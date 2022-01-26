import yaml

from logger import get_logger


logger = get_logger(__name__)


def load_config():
    """
    Converts the configuration file into a dictionary.

    :return: the retrieved dictionary
    :rtype: dict
    """
    with open("configuration.yaml", "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as err:
            logger.error(f"Error upon trying to parse the configuration: {err}")