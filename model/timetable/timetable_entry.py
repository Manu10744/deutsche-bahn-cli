from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeTableEntry:
    """
    Data Object representing an entry in the timetable of a train station.

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