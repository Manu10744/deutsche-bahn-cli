from logger import get_logger

import yaml
import sys


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


def print_more_results(default="yes"):
    """ Asks if the user wants more results to be displayed and returns their answer.

    :param default: the presumed answer if the user just hits <Enter>. It must be "yes" (the default), "no" or None
                    (meaning an answer is required of the user).
    :type default: str

    :return: True for "yes" or False for "no".
    :rtype: bool
    """
    valid_inputs = {"yes": True, "y": True,
                    "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write("\n" + ">>> Would you like to see more results?" + prompt)
        user_choice = input().lower()

        # User didnt input something? Take the default
        if default is not None and user_choice == "":
            return valid_inputs[default]
        elif user_choice in valid_inputs:
            return valid_inputs[user_choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n')." + "\n")
