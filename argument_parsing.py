from argparse import ArgumentParser

import logging


def get_args():
    parser = ArgumentParser(description="A CLI Tool that can be used to retrieve public transport information such as "
                                        "train stations or departures from the official Deutsche Bahn APIs.")

    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument("--verbose",
                                 action="store_const",
                                 dest="loglevel",
                                 const=logging.INFO,
                                 help="Increases the output verbosity.")

    verbosity_group.add_argument("--debug",
                                 action="store_const",
                                 dest="loglevel",
                                 const=logging.DEBUG,
                                 help="Increases the output verbosity to the maximum in order to make debugging easier.")

    core_args_group = parser.add_mutually_exclusive_group()
    core_args_group.add_argument("--search",
                                 type=str,
                                 metavar="<station_name>",
                                 help="Search for train stations by their name. Wildcards (*) can be used. You can "
                                      "search for multiple train stations by seperating the search strings with a comma.")

    core_args_group.add_argument("--timetable",
                                 type=int,
                                 metavar="<station_id>",
                                 help="Display the timetable of the current hour for the train station associated with "
                                      "the given station ID.")

    core_args_group.add_argument("--arrivals",
                                 type=int,
                                 metavar="<station_id>",
                                 help="Display the arrivals at the train station associated with the given station ID.")

    core_args_group.add_argument("--departures",
                                 type=int,
                                 metavar="<station_id>",
                                 help="Display the departures at the train station associated with the given station ID.")
    return parser.parse_args()
