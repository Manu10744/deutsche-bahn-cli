from dotenv import load_dotenv
from logger import get_logger
from DbArgumentParser import DbArgumentParser

logger = get_logger(__name__)


if __name__ == "__main__":
    load_dotenv() # Load API Key

    argparser = DbArgumentParser()
    args = argparser.parse_args()

    logger.info("Script started!")

    if args.hello:
        print("Hello World!")
