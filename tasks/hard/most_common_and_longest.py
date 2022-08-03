"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""


def common_and_longest(text: str) -> tuple:
    from collections import Counter
    split_it = text.split()
    text1 = sorted(split_it, key=len)
    longest = text1[-1]
    Counter = Counter(split_it)
    most_occur = Counter.most_common(1)
    return most_occur[0][0], longest


if __name__ == '__main__':
    print(common_and_longest(
        "привет пока ялюблюpython привет"
    ))
    print('Решено!')
