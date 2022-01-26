from dotenv import load_dotenv
from logger import get_logger
from argument_parsing import DbArgumentParser
from api_client import DbApiClient
from utils import load_config

import sys

logger = get_logger(__name__)


if __name__ == "__main__":
    load_dotenv()  # Load API Key
    sys.stdout.reconfigure(encoding='utf-8')

    argparser = DbArgumentParser()
    args = argparser.parse_args()
    logger.info("Arguments parsed successfully: {}".format(args))

    config = load_config()  # Load configuration
    logger.info("Configuration loaded successfully: {}".format(config))

    api_base_url = config.get("api").get("base_url")
    client = DbApiClient(api_base_url)

    if args.station:
        train_stations = client.search_station(args.station)
        for station in train_stations:
            print("Name: {}".format(station["name"]))
            print("ID: {}".format(station["id"]))
            print("\n")
