from dataclasses import dataclass


@dataclass
class TimeTable:
    """
    Data object representing a timetable of a train station.

    Attributes
    ----------

    train_station : str
        the name of the train station associated with this timetable.
    entries : list
        list of entries, each representing a train arriving and / or departing from `train_station`.
    """

    train_station: str
    entries: list

    def __repr__(self):
        return "Timetable({} - {} entries)".format(self.train_station, len(self.entries))

    def get_sorted_entries(self):
        """
        Returns the timetable entries sorted by the time of arrival.

        :return: the sorted entries.
        """
        return sorted(self.entries)
