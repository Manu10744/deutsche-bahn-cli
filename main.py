from dotenv import load_dotenv
from argument_parsing import DbArgumentParser
from api_client import DbApiClient
from utils import load_config, print_more_results
from datetime import datetime

import os
import sys
import logging


logger = logging.getLogger(__name__)


def main():
    argparser = DbArgumentParser()
    args = argparser.parse_args()

    logging.basicConfig(level=args.loglevel,
                        format='%(asctime)s - %(name)s - %(levelname)s >>> %(message)s',
                        handlers=[logging.StreamHandler()])

    logger.info("Arguments parsed successfully: {}".format(args))

    config = load_config()
    logger.info("Configuration loaded successfully: {}".format(config))

    api_base_url = config.get("api").get("base_url")
    max_results = config.get("output").get("max_results")

    client = DbApiClient(api_base_url)
    if args.search:
        train_stations = client.get_stations(args.search)
        logger.info("Retrieved {} stations!".format(len(train_stations)))

        start_idx = 0
        end_idx = max_results
        while start_idx < len(train_stations):
            for station in train_stations[start_idx:end_idx]:
                print(f"{station['name']} (ID: {station['id']})")

            start_idx += max_results
            if start_idx < len(train_stations) and print_more_results():
                end_idx += max_results
            else:
                break

    elif args.departures:
        departures = client.get_departures(args.departures)

        for departure in departures:
            train_id = departure['name']
            departure_time = datetime.fromisoformat(departure['dateTime']).strftime("%Y-%m-%d %H:%M")

            print(f"{train_id}: Departure at {departure_time}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')

    load_dotenv()
    if 'DB_API_KEY' not in os.environ:
        logger.error("No API Key has been set in the environment!")
        raise SystemExit(1)

    main()
