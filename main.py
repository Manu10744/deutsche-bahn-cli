import os

from dotenv import load_dotenv
from logger import get_logger
from argument_parsing import DbArgumentParser
from api_client import DbApiClient
from utils import load_config

import sys

logger = get_logger(__name__)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')

    load_dotenv()
    if 'DB_API_KEY' not in os.environ:
        logger.error("No API Key has been set in the .env configuration file!")
        raise SystemExit(1)

    argparser = DbArgumentParser()
    args = argparser.parse_args()
    logger.info("Arguments parsed successfully: {}".format(args))

    config = load_config()
    logger.info("Configuration loaded successfully: {}".format(config))

    api_base_url = config.get("api").get("base_url")
    client = DbApiClient(api_base_url)

    if args.search:
        train_stations = client.search_station(args.search)
        for station in train_stations:
            print("Name: {}".format(station["name"]))
            print("ID: {}".format(station["id"]))
            print("\n")
