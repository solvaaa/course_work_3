from src.utils import *
PATH = '../operations.json'


def test_load_data():
    data = load_data(PATH)
    assert isinstance(data, list)


def test_filter_data():
    data = load_data(PATH)
    for transaction in filter_data(data):
        assert transaction.get("state", None) == "EXECUTED"


def test_sort_list():
    data = filter_data(load_data(PATH))
    sorted_data = sort_list(data)
    for i in range(len(sorted_data) - 1):
        assert sorted_data[i]['date'] > sorted_data[i + 1]['date']
