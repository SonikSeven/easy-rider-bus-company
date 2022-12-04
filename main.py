from collections import Counter
from itertools import pairwise

import json
import re


def check_types(database):
    errors = dict.fromkeys(database[0], 0)
    for stop in database:
        if not isinstance(stop["bus_id"], int):
            errors["bus_id"] += 1
        if not isinstance(stop["stop_id"], int):
            errors["stop_id"] += 1
        if not stop["stop_name"] or not isinstance(stop["stop_name"], str):
            errors["stop_name"] += 1
        if not isinstance(stop["next_stop"], int):
            errors["next_stop"] += 1
        if not isinstance(stop["stop_type"], str) or len(stop["stop_type"]) > 1:
            errors["stop_type"] += 1
        if not stop["a_time"] or not isinstance(stop["a_time"], str):
            errors["a_time"] += 1
    errors_number = sum(errors.values())
    print(f"Type and required field validation: {errors_number} errors",
              *(f"{k}: {v}" for k, v in errors.items()), sep="\n")
    if errors_number:
        quit()


def check_format(database):
    errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}
    for stop in database:
        if not re.match(r"[A-Z].* (Road|Avenue|Boulevard|Street)$", stop["stop_name"]):
            errors["stop_name"] += 1
        if stop["stop_type"] not in "SOF":
            errors["stop_type"] += 1
        if not re.match(r"([0-1][0-9]|2[0-4]):[0-5]\d$", stop["a_time"]):
            errors["a_time"] += 1
    errors_number = sum(errors.values())
    print(f"Format validation: {errors_number} errors",
              *(f"{k}: {v}" for k, v in errors.items()), sep="\n")
    if errors_number:
        quit()


def get_lines(database):
    lines = {}
    for i in database:
        lines.setdefault(i["bus_id"], []).append(i)
    return lines


def get_stops(database, stop_type):
    return {stop["stop_name"] for stop in database if stop["stop_type"] == stop_type}


def get_transfers(database):
    stop_names = [stop["stop_name"] for stop in database]
    return {name for name, count in Counter(stop_names).items() if count > 1}


def display_lines(lines, start_stops, transfer_stops, finish_stops):
    for line_id, stops in lines.items():
         stop_types = [stop["stop_type"] for stop in stops]
         if "S" not in stop_types or "F" not in stop_types:
            return print(f"There is no start or end stop for the line: {line_id}.")
    print(f"Start stops: {len(start_stops)} {sorted(list(start_stops))}",
          f"Transfer stops: {len(transfer_stops)} {sorted(list(transfer_stops))}",
          f"Finish stops: {len(finish_stops)} {sorted(list(finish_stops))}", sep="\n")


def get_time_in_minutes(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])


def check_time(lines):
    errors = []
    for line in lines.values():
        for i, j in pairwise(line):
            if get_time_in_minutes(j["a_time"]) <= get_time_in_minutes(i["a_time"]):
                errors.append(f"bus_id line {j['bus_id']}: wrong time on station {j['stop_name']}")
                break
    print("Arrival time test:")
    if errors:
        print(*errors, sep="\n")
    else:
        print("OK")


def check_wrong_stops(on_demand_stops, transfer_stops):
    wrong_stops = sorted(list(on_demand_stops & transfer_stops))
    print("On demand stops test:",
              f"Wrong stop type: {wrong_stops}" if wrong_stops else "OK", sep="\n")


def main():
    with open(input()) as example_file:
        example = example_file.read()
    database = json.loads(example)
    check_types(database)
    check_format(database)
    lines = get_lines(database)
    print("Line names and number of stops:",
          *(f"bus_id: {k}, stops: {len(v)}" for k, v in lines.items()), sep="\n")
    start_stops = get_stops(database, "S")
    on_demand_stops = get_stops(database, "O")
    finish_stops = get_stops(database, "F")
    transfer_stops = get_transfers(database)
    display_lines(lines, start_stops, transfer_stops, finish_stops)
    check_time(lines)
    check_wrong_stops(on_demand_stops, transfer_stops)


if __name__ == '__main__':
    main()
