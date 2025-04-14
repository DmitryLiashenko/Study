from typing import Callable

def caching_fibonacci():        # СОЗДАЕМ ФУНКЦИЮ
    try:                        # НАЧАЛО БЛОКА ОШИБОК
        cache = {}              # СОЗДАЕМ ПУСТОЙ СЛОВАРЬ ДЛЯ КЕШ(КЛЮЧ : ЧИСЛО, VALUE : ФИБОНАЧИ)
        def fibonacci(n):       # СОЗДАЕМ ФУНКЦИЮ ДЛЯ РАСЧЕТА ЧИСЛА ФИБОНАЧИ ПО n
            if n <= 0:          # ПРОВЕРЯЕМ СТАНДАРТНЫЕ РЕШЕНИЯ ДЛЯ ЧИСЛА ФИБОНАЧИ
                return 0        #
            if n == 1:          #
                return 1        #
            if n in cache:      # ЕСЛИ ОТВЕТ УЖЕ ЕСТЬ В КЕШ
                return cache[n] # ДОСТАЕМ ЧИСЛО ПО КЛЮЧУ
            else:               # ЕСЛИ НЕТУ ЧИСЛА, ВЫЧИСЛЯЕМ ПО ФОРМУЛЕ
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
                return cache[n]                                # ВОЗВРАЩАЕМ В КЕШ
        return fibonacci                                       # ВОЗВРАЩАЕМ ФУНКЦИЮ В ФУНКЦИЮ
    except Exception as Error:                                 # КОНЕЦ БЛОКА ОШИБОК
        print(f'Somthing wrong {Error}')                       # СООБЩАЕМ КАКАЯ ОШИБКА