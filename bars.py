import json, argparse, os
from geopy.distance import vincenty


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?', help='Enter filepath to json')
    parser.add_argument('longitude', type=float, help='Enter your longitude')
    parser.add_argument('latitude', type=float, help='Enter your latitude')
    return parser


def load_data_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_data:
        json_string = json.load(json_data)
    return json_string


def get_biggest_bar(json_string):
    return max(json_string, key=lambda fea: fea['SeatsCount'])['Name']


def get_smallest_bar(json_string):
    return min(json_string, key=lambda fea: fea['SeatsCount'])['Name']


def get_closest_bar(json_string, your_place):
    return min(json_string, key=lambda fea: vincenty(fea['geoData']['coordinates'], your_place).kilometers)['Name']


if __name__ == '__main__':
    parsed_args = create_parser()
    args = parsed_args.parse_args()
    loaded_json = load_data_json(args.filepath)
    print("Самый большой - ", get_biggest_bar(loaded_json))
    print("Самый маленький - ", get_smallest_bar(loaded_json))
    longitude, latitude = args.longitude, args.latitude
    your_place = (longitude, latitude)
    print("Самый близкий - ", get_closest_bar(loaded_json, your_place))
