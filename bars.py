import json


file = 'data-2897-2016-11-23.json'


def load_data(filepath):
    with open(filepath) as json_data:
        data = json.load(json_data)
        return data


def pretty_print_json(data):
    form_json = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
    return form_json


def get_biggest_bar(data):
    d = {}
    for bars in data:
        d[bars["Name"]] = bars["SeatsCount"]
    return max(d, key=d.get)


def get_smallest_bar(data):
    d = {}
    for bars in data:
        d[bars["Name"]] = bars["SeatsCount"]
    return min(d, key=d.get)


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    # print(load_data(file))
    # print(pretty_print_json(load_data(file)))
    print(get_biggest_bar(load_data(file)))
    print(get_smallest_bar(load_data(file)))
