from model.timetable.timetable import TimeTable
from utils.io import print_more_results


def print_stations(train_stations: list, max_results: int):
    if len(train_stations) == 0:
        print("No train stations were found.")

    print("\nFound train stations:\n")

    idx = 0
    end_idx = max_results
    while idx < len(train_stations):
        for station in train_stations[idx:end_idx]:
            print(station)
            idx += 1

        if idx < len(train_stations) and print_more_results():
            end_idx += max_results
        else:
            break


def print_timetable(timetable: TimeTable, max_results: int):
    entries = timetable.get_sorted_entries()
    if len(entries) == 0:
        print("No timetable data for that train station.")

    print(f"\nThe Timetable for {timetable.train_station}:\n")

    idx = 0
    end_idx = max_results
    while idx < len(entries):
        for entry in entries[idx:end_idx]:
            print(entry)
            idx += 1

        if idx < len(entries) and print_more_results():
            end_idx += max_results
        else:
            break
