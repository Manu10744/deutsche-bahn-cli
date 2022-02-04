from dataclasses import dataclass


@dataclass
class TrainStation:
    """
    Data object representing a train station.

    Attributes
    ----------

    name : str
        the official name of this train station.
    eva_numbers : list
       a list of eva-numbers associated with this train station.
    """

    name: str
    eva_numbers: list

    def __repr__(self):
        return f"TrainStation({self.name} - {self.eva_numbers})"
