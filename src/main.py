from utils import *
PATH = '../operations.json'


def main(path):
    data = load_data(path)
    filtered = filter_data(data)
    sorted_data = sort_list(filtered)
    #for i in sorted_data[:5]:
    #    print(print_transaction(i))
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
    print(print_transaction(transaction))



if __name__ == "__main__":
    main(PATH)