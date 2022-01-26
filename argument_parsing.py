from argparse import ArgumentParser


class DbArgumentParser(ArgumentParser):
    """
    The ArgumentParser for the CLI.
    """

    def __init__(self):
        super().__init__()
        self.add_argument("--search", help="Search for either the full name or a fracture of the name of a train station.")

