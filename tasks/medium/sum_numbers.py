"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет результат сложения цифр целого числа

ПРИМЕРЫ
--------------------------------------------------------------------------------
num_sum(5216) -> 14
num_sum(58716) -> 27
num_sum(321) -> 6
"""


def num_sum(numb: int) -> int:
    summa = 0
    while (numb != 0):
        summa = summa + (numb % 10)
        numb = numb // 10

    return sum


if __name__ == '__main__':
    assert num_sum(5216) == 14
    print('Решено!')
