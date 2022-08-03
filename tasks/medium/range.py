"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию list_compose, которая принимает два списка (INDEX_LIST, VALUE_LIST).
Составить новый список: берем индекс из списка индексов, и вставляем значение по этому
индексу из другого списка. Если значения нет, что вставить None

ПРИМЕРЫ
--------------------------------------------------------------------------------
list_compose(INDEX_LIST, VALUE_LIST) -> ['b', 'f', None, None, 'c', 'd', None, 'e']
"""
INDEX_LIST = [1, -1, 6, -12, 2, 3, 9, 4]
VALUE_LIST = ['a', 'b', 'c', 'd', 'e', 'f']


def list_compose(indexes: list, values: list) -> list:
    result_list = []
    for i in range(len(indexes)):
        try:
            znachenie = values[indexes[i]]
        except ValueError and IndexError:
            znachenie = None
        result_list.append(znachenie)
    return result_list


if __name__ == '__main__':
    print(list_compose(INDEX_LIST, VALUE_LIST))
    print('Решено!')
