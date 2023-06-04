from utils import *
PATH = '../operations.json'


def main(path):
    data = load_data(path)
    filtered = filter_data(data)
    sorted_data = sort_list(filtered)
    for i in sorted_data[:5]:
        print(print_transaction(i))


if __name__ == "__main__":
    main(PATH)