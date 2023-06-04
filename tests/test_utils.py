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


def test_format_id():
    assert format_id("Счет 11492155674319392427") == 'Счет **2427'
    assert format_id("Visa Mastercard 1234567891011121") == 'Visa Mastercard 1234 56** **** 1121'