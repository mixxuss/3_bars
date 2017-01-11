import json
from geopy.distance import vincenty


def load_data(filepath):
    # Loads JSON file from filepath variable and return it in str
    with open(filepath) as json_data:
        data = json.load(json_data)
        return data


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


def get_closest_bar(data, longitude, latitude):
    # Gets a str variable with data, longitude and latitude from input and return the closest value key
    d = {}
    your_place = (longitude, latitude)
    for bars in data:
        li = tuple(bars["geoData"]["coordinates"])
        d[bars["Name"]] = vincenty(li, your_place).kilometers
    return min(d, key=d.get)


if __name__ == '__main__':
    # Put a path to file to file variable
    file = 'data-2897-2016-11-23.json'
    print("Самый большой - ", get_biggest_bar(load_data(file)))
    print("Самый маленький - ", get_smallest_bar(load_data(file)))
    longitude, latitude = float(input("longitude is ")), float(input("latitude is "))
    print("Самый близкий - ", get_closest_bar(load_data(file), longitude, latitude))
