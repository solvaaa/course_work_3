import json
from datetime import datetime


def load_data(path):
    """загружает файл с данными"""
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def filter_data(data):
    """фильтрует по ключам ['EXECUTED']"""
    filtered_data = []
    for transaction in data:
        if transaction.get("state", None) == "EXECUTED":
            filtered_data.append(transaction)
    return filtered_data


def get_data(datum):
    """возвращает дату транзакции"""
    date = datum.get("date", '')
    return date


def sort_list(data):
    """сортирует по датам"""
    sorted_data = sorted(data, key=get_data, reverse=True)
    return sorted_data


def print_transaction(transaction):
    """возвращает строку для печати в нужном формате"""
    date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')
    date_string = date.strftime('%d.%m.%Y')
    output = f'{date_string} {transaction["description"]}\n'
    if 'from' in transaction:
        output += f'{format_id(transaction["from"])} -> {format_id(transaction["to"])}\n'
    else:
        output += f'{format_id(transaction["to"])}\n'
    output += f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n"
    return output


def format_id(account_id):
    """изменяет старый формать данных (номер счёта/карты) на нужный"""
    id_list = account_id.split()
    id = id_list[-1]
    name_card = ' '.join(id_list[0:-1])
    if len(id) == 16:
        formatted = id[:4] + ' ' + id[4:6] + '** **** ' + id[12:]
    else:
        formatted = '**' + id[-4:]
    return name_card + ' ' + formatted

