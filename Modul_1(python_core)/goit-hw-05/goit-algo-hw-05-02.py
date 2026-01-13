# Можно было сделать как преподаватель, но хотел от из Своей головы)) согласно стандарту PEP8 - больше текста чем кода :-)))

import re
from typing import Callable
from functools import reduce


def generator_numbers(text: str):
    """
    Генератор, извлекающий числа с плавающей точкой из текста.
    """
    pattern = r"\d+[.]\d+"                # ИСПОЛЬЗУЕМ raw-СТРОКУ КАК ПАТЕРН
    numbers = re.findall(pattern, text)   # СОЗДАЕМ СПИСОК ИЗ НАЙДЕНОЙ ИНФОРМАЦИИ СОГЛАСНО ПАТЕРНУ
    for number in numbers:                # ИТЕРИРУЕМ СПИСОК 
        yield float(number)               # ВОЗВРАЩАЕМ В ФУНКЦИЮ ЧИСЛО(float) И ЗАПОМИНЕМ СОСТОЯНИЕ ФУНКЦИИ


def sum_profit(text: str, func: Callable):
    """
    Функция, вычисляющая сумму чисел, извлеченных из текста с помощью переданной функции.
    """
    return reduce(lambda x, y: x + y, func(text)) # Используем reduce для суммирования результатов функции


text = "Загальний дохід працівника складається з декількох частин: 1000.01\
        як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

print(f"Загальний дохід: {sum_profit(text, generator_numbers)}")