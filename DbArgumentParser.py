from argparse import ArgumentParser


class DbArgumentParser(ArgumentParser):
    """
    The ArgumentParser for the CLI.
    """

    def __init__(self):
        super().__init__()
        self.add_argument("--hello", action="store_true")

