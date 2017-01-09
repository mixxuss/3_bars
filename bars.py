import json
from urllib.request import urlopen

#url='http://op.mos.ru/EHDWSREST/catalog/export/get?id=84505'
file = 'data-2897-2016-11-23.json'


def load_data(filepath):
    # response = urlopen(filepath)
    # data = response.read()#.decode('utf-8')
    # return json.loads(data)
    data = json.loads(filepath)
    text_data = data.read()
    return text_data


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    print(load_data(file))
