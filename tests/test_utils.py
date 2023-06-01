from src.utils import *
PATH = '../operations.json'


def test_load_data():
    data = load_data(PATH)
    assert isinstance(data, list)


def test_filter_data():
    data = load_data(PATH)
    for transaction in filter_data(data):
        assert transaction.get("state", None) == "EXECUTED"
