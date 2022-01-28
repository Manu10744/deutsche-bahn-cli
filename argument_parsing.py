from argparse import ArgumentParser

import logging

class DbArgumentParser(ArgumentParser):
    """
    The ArgumentParser for the CLI.
    """

    def __init__(self):
        super().__init__()

        self.description = "A CLI Tool that can be used to retrieve public transport information such as train stations \
                           or departures from the official Deutsche Bahn APIs. See below how to use it."

        group = self.add_mutually_exclusive_group()
        group.add_argument("--verbose",
                           action="store_const",
                           dest="loglevel",
                           const=logging.INFO,
                           help="Increases the output verbosity.")

        group.add_argument("--debug",
                           action="store_const",
                           dest="loglevel",
                           const=logging.DEBUG,
                           help="Increases the output to the maximum in order to make debugging easier.")

        group.add_argument("--search",
                           type=str,
                           metavar="<station_name>",
                           help="Get information about a train station by searching with either the full name or a \
                                 fracture of it.")

        group.add_argument("--departures",
                           type=int,
                           metavar="<station_id>",
                           help="Get the departures for the train station corresponding to the given ID.")
