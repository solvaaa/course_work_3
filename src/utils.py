import json


def load_data(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data



