import json
from geopy.distance import vincenty


file = 'data-2897-2016-11-23.json'


def load_data(filepath):
    # Loads JSON file from filepath variable and return it in str
    with open(filepath) as json_data:
        data = json.load(json_data)
        return data


def pretty_print_json(data):
    # Gets a str variable with data and return it pretty view
    form_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    return form_json


def get_biggest_bar(data):
    # Gets a str variable with data and return max value key
    d = {}
    for bars in data:
        d[bars["Name"]] = bars["SeatsCount"]
    return max(d, key=d.get)


def get_smallest_bar(data):
    # Gets a str variable with data and return min value key
    d = {}
    for bars in data:
        d[bars["Name"]] = bars["SeatsCount"]
    return min(d, key=d.get)


def get_closest_bar(data, longitude=33, latitude=22):
    d = {}
    for bars in data:
        d[bars["Name"]] = bars["geoData"]["coordinates"]
    li = []
    for bars in d.keys():
        li.append(bars)
        li = li + d[bars]
    your_place = (longitude, latitude)
    for bars in d.values():
        print(vincenty(bars, your_place))
        print(bars)
    return d


if __name__ == '__main__':
    # print(load_data(file))
    print(pretty_print_json(load_data(file)))
    # print(get_closest_bar(load_data(file)))
    # print(get_biggest_bar(load_data(file)))
    # print(get_smallest_bar(load_data(file)))
    print(get_closest_bar(load_data(file)))
