import json
from datetime import datetime

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


def get_data(datum):
    date = datum.get("date", '')
    return date


def sort_list(data):
    sorted_data = sorted(data, key=get_data, reverse=True)
    return sorted_data


def print_transaction(transaction):
    date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')
    date_string = date.strftime('%d.%m.%Y')
    print(date_string, transaction["description"])
    print(format_id(transaction['from']), ' -> ', format_id(transaction['to']))
    print(transaction['operationAmount']['amount'], transaction['operationAmount']['currency']['name'])


def format_id(account_id):
    id_list = account_id.split()
    id = id_list[-1]
    name_card = ' '.join(id_list[0:-1])
    if len(id) == 16:
        formatted = id[:4] + ' ' + id[4:6] + '** ****' + id[12:]
    else:
        formatted = '**' + id[-4:]
    return name_card + ' ' + formatted



#print(date_string, transaction["description"])
#14.10.2018 Перевод организации
#Visa Platinum 7000 79** **** 6361 -> Счет **9638
#82771.72 руб.
#path = '../operations.json'
#data = filter_data(load_data(path))
print_transaction( {
    "id": 710136990,
    "state": "CANCELED",
    "date": "2018-08-17T03:57:28.607101",
    "operationAmount": {
      "amount": "66906.45",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 1913883747791351",
    "to": "Счет 11492155674319392427"
  })