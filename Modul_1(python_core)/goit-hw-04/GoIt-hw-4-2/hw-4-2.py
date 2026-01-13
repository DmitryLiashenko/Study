                                    # ФУНКЦИЯ СОЗДАЕТ СПИСОК СЛОВАРЕЙ С ДАННЫМИ ИЗ ФАЙЛА ЧЕРЕЗ ЗЯПЯТУЮ С ПЕРЕНОСОМ

from pathlib import Path                                  # ИМПОРТИРУЕМ МЕТОД ИЗ МОДУЛЯ

def get_cats_info(path = None):                           # СОЗДАЕМ ФУНКЦИЮ
    try:                                                  # НАЧАЛО БЛОКА ОЩИБОК
        list_cats = []                                    # СОЗДАЕМ ПУСТОЙ СПИСОК
        with open(path, encoding='utf-8') as fh:          # ОТКРЫВАЕМ ФАЙЛ С ПОМОЩЬЮ МЕНЕДЖЕРА КОНТЕКСТОВ
            lines = [el.strip() for el in fh.readlines()] # РАЗДЕЛЯЕМ НАКЖДУ СТРОКУ В ТЕКСТЕ
            for line in lines:                            # ПРОХОДИМСЯ ПО ЭЛЕМЕНТАМ КАЖДОЙ СТРОКИ
                separator = line.split(',')               # РАЗДЕЛЯЕМ ТЕКСТ ПО ПАТЕРНУ ","
                list_cats.append({'id': separator[0], 'name' : separator[1], 'age' : separator[2]}) # ДОБАВЛЯЕМ В СЛОВАРЬ НУЖНЫЕ ДАННЫЕ
        return list_cats                                                                            # ВОЗВРАЩАЕМ СПИСОК СЛОВАРЕЙ
    except Exception as Error:                                                                      # КОНЕЦ БЛОКА ОШИБОК
        print (f'something bad {Error}')                                                            # СООБЩАЕМ ОБ ОШИБКЕ
print(get_cats_info(r'D:\IT\Repositorys\goit-algo-hw-04\GoIt-hw-4-2\cats.txt.txt'))                 # ТЕСТ