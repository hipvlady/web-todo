FILEPATH = "todos.txt"


def get_item(filepath=FILEPATH):
    with open(FILEPATH, 'r') as file_local:
        items_local = file_local.readlines()
        return items_local


def write_item(item_arg, filepath=FILEPATH):
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(item_arg)


if __name__ == '__main__':
    print(get_item())
