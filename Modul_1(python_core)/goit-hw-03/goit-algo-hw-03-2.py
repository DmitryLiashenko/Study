                            #  Функция для генерирования случайных чисел для лотереи
import random
def get_numbers_ticket(min, max, quantity):                         # СОЗДАЕМ ФУНКЦИЮ
    if min < max and min >= 1 and max <=1000 and quantity <= max :  # ПРОВЕРЯЕМ СООТВЕТСВУЮТ ЛИ ПАРАМЕТРЫ           
        list_with_lotery_digits = []                                # СОЗДАЕМ ПУСТОЙ СПИСОК           
        while quantity >= 1:                                        # ЗАПУСКАЕМ ЦИКЛ С НУЖНЫМ КОЛЛИЧЕСТВОМ ПОВТОРЕНИЙ                                  
            random_digit = random.randint(min, max)                 # ПОЛУЧАЕМ СЛУЧАЙНОЕ ЧИСЛО ИЗ ЗАДАНООГО ДИАПАЗОНА
            if random_digit not in list_with_lotery_digits:         # ПРОВЕРЯЕМ ЧТО БЫ ЭТО ЧИСЛО УЖЕ НЕ БЫЛО В СПИСКЕ                        
                list_with_lotery_digits.append(random_digit)        # ДОБАВЛЯЕМ ЧИСЛО В СПИСОК           
                quantity = quantity - 1                             # УМЕНШАЕМ ИТЕРАЦИЮ ЦИКЛА НА 1 (если число уже есть в списке,то итерация не уменшается)
        return sorted(list_with_lotery_digits)                      # СОРТИРУЕМ СПИСОК И ВОЗВРАЩАЕМ В ФУНКЦИЮ   
    else:                                                           # КОНЕЦ ЦИКЛА if
            print("Числа выходят из заданного диапазон\n\
Минимальное значение 1, максимальное 1000\n\
Колличество желаемых чисел не больше 1000 ")                        # ВЫВОДИМ ПРЕДУПРЕЖДЕНИЕ ЕСЛИ ЗАДАННЫЕ АРГУМЕНТЫ НЕ СООТВЕТСВУЮТ ДИАПАЗОНУ
print(get_numbers_ticket(11, 150, 10))
