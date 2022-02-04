from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeTableEntry:
    """
    Data Object representing an entry in the timetable of a train station. An entry in the timetable is a train
    arriving and/or departing from the timetable's train station.

    Attributes
    ----------

    train : str
        the name of the train representing the timetable entry
    arrival_time : datetime
        the time of arrival, if this entry is not the start of the associated journey.
    departure_time : datetime
        the time of departure, if this entry is not the last stop of the associated journey.
    route : list
        the list of stops representing the path of the associated journey.
    """

    train: str
    arrival_time: datetime
    departure_time: datetime
    route: list

    def __repr__(self):
        return "TimeTableEntry({} - Arrival {} - Departure {})".format(self.train, self.arrival_time, self.departure_time)

    def __lt__(self, other):
        """
        Compare two timetable entries by departure time. If there is no departure time, it means the entry represents
        the end of the journey, so these are considered to be last.

        :param other: the other `TimeTableEntry`.
        """
        if self.is_terminus():
            if other.is_terminus():
                # Both are the last stops, so sort by arrival time
                return self.arrival_time < other.arrival_time
            else:
                # self is last stop, other is not, so put self last.
                return False

        if other.is_terminus():
            # Other is last stop, so put it last
            return True
        else:
            # Both are ordinary stops
            return self.departure_time < other.departure_time

    def is_begin(self) -> bool:
        """
        Returns whether this `TimeTableEntry` is the beginning of its associated journey.

        :return: True if this entry represents the beginning, otherwise False.
        """
        return self.arrival_time is None

    def is_terminus(self) -> bool:
        """
        Returns whether this `TimeTableEntry` is the terminus of its associated journey.

        :return: True if this entry represents the terminus, otherwise False.
        """
        return self.departure_time is None



