# ФУНКЦЫЯ ДЛЯ РАСЧЕТА СУММЫ И СРЕДНЕЙ ЗП

from pathlib import Path                              # Импортируем метод для работы с путем к фалам
def total_salary(path = None): 
    try:                       # Создаем функцию
        payroll = []                                      # СОЗДАЕМ ПУСТОЙ СПИСОК
        with open(path, encoding='utf-8') as fh:          # ОТКРЫВАЕМ ФАЙЛ ДЛЯ СЧИТЫВАНИЯ
            lines = [el.strip() for el in fh.readlines()] # РАЗДЕЛЯЕМ ПО СТРОКАМ
            sum = 0                                       
            col = 0                                       
            for line in lines:                            # ИТЕРИРУЕМ КАЖДУЮ СТРОКУ
                separator = line.split(',')               # ОПРЕДЕЛЯЕМ РАЗДЕЛ ПО ПАТЕРНАМ
                sum = sum + int(separator[1])             # СУМИРУЕМ ЗАРПЛАТЫ
                col = col + 1                             # СЧИТАЕМ КОЛ-ВО СОТРУДНИКОВ
            sr = sum / col                                # ВЫЧИСЛЯЕМ СРЕДНЮЮ СУММУ
            payroll.append(sum)                           # ДОБАВЛЯЕМ В СПИСОК СУММУ
            payroll.append(int(sr))                       # ДОБАВЛЯЕМ В СПИСОК СРЕДНЕЕ
        print(f'Общая сумма заработной платы {sum}, Средняя зарплата {int(sr)}')   # ПРИНТИМ РЕЗУЛЬТАТ
        return payroll                                                             # ВОЗВРАЩАЕМ СПИСОК В ФУНКЦИЮ
    except Exception as Error:                                                     # КОНЕЦ БЛОКА ОБРАБОТКИ ОШИБОК
        print (f'something bad {Error}')                                           # ВЫВОДИМ СООБЩЕНИЕ ОБ ОШИБКЕ                      
print(total_salary(r"goit-algo-hw-04/GoIT-hw-4-1/file1.txt.txt"))  # ТЕСТ
