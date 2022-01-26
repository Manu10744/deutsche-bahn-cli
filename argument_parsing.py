from argparse import ArgumentParser


class DbArgumentParser(ArgumentParser):
    """
    The ArgumentParser for the CLI.
    """

    def __init__(self):
        super().__init__()
        self.description = "A CLI Tool that makes it possible to retrieve public transport information such as \
                           train stations or departures from the official Deutsche Bahn APIs. See below how to use it."
        self.add_argument("--search",
                          type=str,
                          metavar="<station_name>",
                          help="Get information about a train station by searching with either the full name" +
                               " or a fracture of it.")

        self.add_argument("--departures",
                          type=int,
                          metavar="<station_id>",
                          help="Get the departures for the train station corresponding to the given ID.")