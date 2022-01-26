from argparse import ArgumentParser


class DbArgumentParser(ArgumentParser):
    """
    The ArgumentParser for the CLI.
    """

    def __init__(self):
        super().__init__()
        self.add_argument("--station", help="Either the full name or a fracture of the name of the train station that is searched.")

