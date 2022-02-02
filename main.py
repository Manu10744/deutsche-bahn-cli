from dotenv import load_dotenv
from argument_parsing import DbArgumentParser
from api_client import DbApiClient
from utils.io import load_config, print_more_results

import os
import logging


logger = logging.getLogger(__name__)


def print_stations(train_stations, max_results):
    print("\nFound train stations:\n")

    idx = 0
    end_idx = max_results
    while idx < len(train_stations):
        for station in train_stations[idx:end_idx]:
            print(f"{station['name']} \t (ID: {station['id']})")
            idx += 1

        if idx < len(train_stations) and print_more_results():
            end_idx += max_results
        else:
            break


def print_departures(timetable, max_results):
    print(f"\nFound departures for {timetable.train_station}:\n")

    idx = 0
    end_idx = max_results
    while idx < len(timetable.entries):
        for entry in timetable.entries[idx:end_idx]:
            print("{}: Departure at {}".format(entry.train, entry.departure_time))
            print(" | ".join(entry.route))
            print("\n")
            idx += 1

        if idx < len(timetable.entries) and print_more_results():
            end_idx += max_results
        else:
            break


def main():
    argparser = DbArgumentParser()
    args = argparser.parse_args()
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

        if len(train_stations) > 0:
            print_stations(train_stations, max_results)
        else:
            print("No train stations were found.")

    elif args.departures:
        station_id = args.departures
        timetable = client.get_departures(station_id)

        print_departures(timetable, max_results)


if __name__ == "__main__":
    load_dotenv()

    if 'DB_API_KEY' not in os.environ:
        logger.error("No API Key has been set in the environment!")
        raise SystemExit(1)

    main()
