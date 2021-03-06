from dotenv import load_dotenv
from argument_parsing import get_args
from api_client import DbApiClient
from utils.io import load_config
from utils.printing import print_stations, print_timetable, print_arrivals, print_departures

import os
import logging


logger = logging.getLogger(__name__)


def main():
    args = get_args()
    logger.info("Arguments parsed successfully: {}".format(args))

    logging.basicConfig(level=args.loglevel, format='%(asctime)s - %(name)s - %(levelname)s >>> %(message)s',
                        handlers=[logging.StreamHandler()])

    config = load_config()
    logger.info("Configuration loaded successfully: {}".format(config))

    api_base_url = config.get("api").get("base_url")
    max_results = config.get("output").get("max_results")

    client = DbApiClient(api_base_url)
    if args.search:
        search_string = args.search
        train_stations = client.get_stations(search_string)

        print_stations(train_stations, max_results)

    elif args.timetable:
        station_id = args.timetable
        timetable = client.get_timetable(station_id)
        print_timetable(timetable, max_results)

    elif args.arrivals:
        station_id = args.arrivals
        timetable = client.get_timetable(station_id)
        print_arrivals(timetable.get_arrivals())

    elif args.departures:
        station_id = args.departures
        timetable = client.get_timetable(station_id)
        print_departures(timetable.get_departures())


if __name__ == "__main__":
    load_dotenv()

    if 'DB_API_KEY' not in os.environ:
        logger.error("No API Key has been set in the environment!")
        raise SystemExit(1)

    main()
