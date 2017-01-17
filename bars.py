import json, argparse, os
from geopy.distance import vincenty


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')
    return parser


def load_data_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_data:
        json_string = json.load(json_data)
    return json_string


def make_dict_seatscount(json_string):
    return {bars["Name"] : bars["SeatsCount"] for bars in json_string}


def make_dict_range(json_string, longitude, latitude):
    your_place = (longitude, latitude)
    dict_range = {bars["Name"] : vincenty(tuple(bars["geoData"]["coordinates"]), your_place).kilometers for bars in json_string}
    return dict_range


def get_biggest_bar(dict_seatscount):
    return max(dict_seatscount, key=dict_seatscount.get)


def get_smallest_bar(dict_seatscount):
    return min(dict_seatscount, key=dict_seatscount.get)


def get_closest_bar(dict_range):
    return min(dict_range, key=dict_range.get)


if __name__ == '__main__':
    parsed_args = create_parser()
    filepath = parsed_args.parse_args()
    loaded_json = load_data_json(filepath.filepath)
    dict_seatscount = make_dict_seatscount(loaded_json)
    print("Самый большой - ", get_biggest_bar(dict_seatscount))
    print("Самый маленький - ", get_smallest_bar(dict_seatscount))
    longitude, latitude = float(input("longitude is ")), float(input("latitude is "))
    dict_range = make_dict_range(loaded_json, longitude, latitude)
    print("Самый близкий - ", get_closest_bar(dict_range))
