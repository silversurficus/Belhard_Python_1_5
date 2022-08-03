"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать программу, которая будет выводить количество четных и нечетных значений
в списке из целых чисел

even - четные
odd - нечетные
"""


def calc_even_odd(array: list) -> tuple:
    def get_even_numbers(numbers):
        even_numbers = []

        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)

        return even_numbers

    def get_odd_numbers(numbers):
        odd_numbers = []

        for number in numbers:
            if number % 2 == 1:
                odd_numbers.append(number)

        return odd_numbers
    even = len(get_even_numbers(array))
    odd = len(get_odd_numbers(array))
    return even, odd


if __name__ == '__main__':
    assert calc_even_odd([2, 1, 5, 4, 7]) == (2, 3)
    print('Решено!')
