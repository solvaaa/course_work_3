from src.utils import *
PATH = '../operations.json'
def get_transaction():
    transaction = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
      "amount": "96995.73",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 27248529432547658655",
    "to": "Счет 97584898735659638967"
    }
    return transaction


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


def test_print_transaction():
    transaction = get_transaction()
    expected_result = "14.04.2018 Перевод организации" + "\n"
    expected_result += "Счет **8655 -> Счет **8967" + "\n"
    expected_result += "96995.73 руб." + "\n"
    assert print_transaction(transaction) == expected_result