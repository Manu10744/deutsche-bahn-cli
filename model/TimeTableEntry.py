from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeTableEntry:
    """
    Data Object for an entry in the timetable retrieved from the Deutsche Bahn TimeTable API.
    """

    train: str
    arrival_time: datetime
    departure_time: datetime
    route: list

    def __init__(self, train, arrival_time, departure_time, route):
        """
        Constructor.

        :param train: a train represented by the kind of train followed by an identifying numeric
                      value,  e.g. ICE 502
        :type train: str
        :param arrival_time: the time of arrival at the `train_station`.
        :type arrival_time: datetime
        :param departure_time: the time of departure from the `train_station`.
        :type departure_time: datetime
        :param route: a list containing all train stations
        :type route: list of strings
        """
        self.train = train
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.route = route

    def __repr__(self):
        return "TimeTableEntry({} - Arrival {} - Departure {})".format(self.train, self.arrival_time, self.departure_time)