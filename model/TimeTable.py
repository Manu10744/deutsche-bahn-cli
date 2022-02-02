from xml.etree import ElementTree
from model.TimeTableEntry import TimeTableEntry
from utils.time import parse_datetime

from dataclasses import dataclass


@dataclass
class TimeTable:
    """ Data object for a TimeTable retrieved from the Deutsche Bahn TimeTable API. """

    train_station: str
    entries: list

    def __init__(self, train_station, entries):
        """
        Constructor.

        :param train_station: the train station corresponding to this timetable.
        :type train_station: str
        :param entries: the entries for that timetable, each representing a train with arrival and
                        departure data.
        :type entries: list of `TimeTableEntry`
        """
        self.train_station = train_station
        self.entries = entries

    def __repr__(self):
        return "Timetable({} - {} entries)".format(self.train_station, len(self.entries))

    @classmethod
    def from_xml_string(cls, xml_string):
        """
        Constructs a `TimeTable` from the given XML string.

        :param xml_string: the string representing the timetable in XML.
        :type xml_string: str

        :return: a corresponding `TimeTable`.
        """
        timetable_tree = ElementTree.fromstring(xml_string)
        table_train_station = timetable_tree.get("station")

        entries = list()
        for train_entry in timetable_tree:
            train_details = train_entry.find("tl")
            train_type = train_details.get("c")
            train_number = train_details.get("n")

            arrival = train_entry.find("ar")
            departure = train_entry.find("dp")

            route = list()
            if arrival is not None:
                path_before_arrival = arrival.get("ppth").split("|")
                for train_station in path_before_arrival:
                    route.append(train_station)

            route.append(table_train_station)

            if departure is not None:
                path_after_departure = departure.get("ppth").split("|")
                for train_station in path_after_departure:
                    route.append(train_station)

            entry = TimeTableEntry(
                train=f"{train_type} {train_number}",
                arrival_time=parse_datetime(arrival.get("pt")) if arrival is not None else None,
                departure_time=parse_datetime(departure.get("pt")) if departure is not None else None,
                route=route
            )
            entries.append(entry)

        return cls(table_train_station, entries)
