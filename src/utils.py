import json


def load_data(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def filter_data(data):
    filtered_data = []
    for transaction in data:
        if transaction.get("state", None) == "EXECUTED":
            filtered_data.append(transaction)
    return filtered_data


def imported_list(data):
    sorted_data = sorted(data)
    return sorted_data
