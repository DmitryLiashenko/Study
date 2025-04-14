# # length = float(input("lenght"))
# # width = float(input("width"))
# # area = length*width
# # show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# # print(show)

# # name = "Dmitry"
# # age = 34
# # is_active = True
# # subscription = ()

# # name = input("Your name? ")
# # email = input("Your email? ")
# # age = int(input("Your age? "))
# # height = float(input("Your height? "))
# # is_active =  True

# #Списки
# # my_list = []
# # my_list = [2024, 3.12]
# # some_data = ['Python']
# # my_list.extend(some_data)
# # # my_list.insert(1, 'Python')
# # # my_list.reverse()
# # print(my_list)

# #Slovnik
# # data = {"year": 2024, "lang": "Python", "version": 3.12}

# # cat = {"nick": "Simon", "age": 7, "characteristics": ["лагідний", "кусається"]}
# # info = {"status": "vaccinated", "breed": True}
# # age = cat.get("age")
# # cat.update(info)
# # print(cat)


#                                     # 1 MODUL 1 LESSON

# #a = 2.2
# #print(type(a))

# # a = None
# # print(type(a))
# # <class 'NoneType'>

# #____a = 4
# #print(a )

# # a = input("chislo : ")
# # b = input("chislo : ")
# # print(f"sum {int(a)+int(b)}")

#                                   # 1 MODUL 2 LESSON

#                                   # 2 MODUL 1 LESSON

# # def greet(name: str) -> str:
# #     return f"Привіт, {name}!"

# # greeting = greet("Олексій")
# # print(greeting)  # Виведе: Привіт, Олексій!

# # def modify_string(original: str) -> str:
# #     original = "змінено"
# #     return original

# # str_var = "оригінал"
# # print(modify_string(str_var))  # виведе: змінено
# # print(str_var)                # виведе: оригінал

# # def string_to_codes(string: str) -> dict:
# #     # Ініціалізація словника для зберігання кодів
# #     codes = {}  
# #     # Перебір кожного символу в рядку
# #     for ch in string:  
# #         # Перевірка, чи символ вже є в словнику
# #         if ch not in codes:
# #             # Додавання пари символ-код в словник  
# #             codes[ch] = ord(ch)  
# #     return codes

# # result = string_to_codes("qwertyuiopoijhgfdsazxcvbnmm")
# # print(result)

# # x = 50

# # def func() -> None:
# #     x = 2
# #     print('Зміна локального x на', x)  # Зміна локального x на 2

# # func()
# # print('Глобальний x як і раніше', x)  # x як і раніше 50

# # def func_outer():
# #     x = 2

# #     def func_inner():
# #         nonlocal x
# #         x = 5

# #     func_inner()
# #     return x

# # result = func_outer()  # 5

# # x = 50

# # def func():
# #     global x
# #     print('x дорівнює', x)  # x дорівнює 50
# #     x = 2
# #     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# # func()
# # print('Значення x складає', x)# Значення x складає 2

# # def greet(name, message="Привіт"):
# #     print(f"{message}, {name}!")

# # greet("Dima")
# # greet("Olia", message="Hi")

# # def func(a, b=5, c=10):
# #     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# # func(3, 7)

# # # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# # func(25, c=24)

# # # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# # func(c=50, a=100)

# # def print_all_args(*args):
# #     for arg in args:
# #         print(arg)

# # print_all_args(1, 'hello', True)

# # def factorial(n):
# #     if n == 0: # базовий випадок
# #         return 1
# #     else:
# #         return n * factorial(n-1) # рекурсивний випадок

# # print(factorial(5)) # виведе 120

# # def factorial(n):
# #     print("Виклик функції factorial з n = ", n)
# #     if n == 1:
# #         print("Базовий випадок, n = 1, повернення 1")
# #         return 1
# #     else:
# #         result = n * factorial(n-1)
# #         print("Повернення результату для n = ", n, ": ", result)
# #         return result

# # print(factorial(15))

# # is_next = None
# # num = int(input("Enter the number of points: "))
# # if num >= 83:
# #     is_next = True
# # else:
# #     is_next = False

# # work_experience = int(input("Enter your full work experience in years: "))

# # if work_experience > 5:
# #     developer_type = "Senior"
# # elif work_experience >1 :
# #     developer_type = "Middle"
# # else :
# #     developer_type = "Junior"
# # print(developer_type)

# # num = int(input("Enter a number: "))

# # if num > 0 :
# #     if  num % 2 == 0 :
# #         result = "Positive odd number"
# #     else:
# #         result = "Positive even number"
# # elif num < 0 :
# #         result = "Negative number"
# # else:
# #         result = "It is zero"
# # print(result)

# # num = int(input("Enter the integer (0 to 100): "))
# # sum = 0

# # while num >= 0:
# #     sum = sum + num
# #     num = num - 1    
# # print(sum)

# # message = "Never argue with stupid people, they will drag you down to\
# #             their level and then beat you with experience."
# # search = "r"
# # result = 0
# # for chair in message:
# #     if chair == search:
# #         result = result + 1
# # print(result)
  
# # pool = 1000
# # quantity = int(input("Enter the number of mailings: "))
# # try:
# #     chunk = pool / quantity  
# #     chunk = int(chunk)
# # except ZeroDivisionError:
# #         print('Delenie na nol!')   
# # else:
# #      print(chunk)
# # val = 'a'
# # try:
# #     val = int(val)
# # except ValueError:
# #     print(f"val {val} is not a number")
# # else:
# #     print(val > 0)
# # finally:
# #     print("This will be printed anyway") 

# # age = input("How old are you? ")
# # try:
# #     age = int(age)
# #     if age >= 18:
# #         print("You are adult.")
# #     else:
# #         print("You are infant")
# # except ValueError:
# #     print(f"{age} is not a number")

# # def greeting():
# #         print('"Hello world"')
# # greeting()

# # def invite_to_event(username):
# #     username = input("Vvedite imya : ")
# #     return username
# #     print(f"Dear {username}, we have the honour to invite you to our event")              
# # invite_to_event()

# # def invite_to_event(username):
# #     print(f"Dear {username}, we have the honour to invite you to our event") 
# #     return username
# # invite_to_event(username = input("vvedite imya : "))

# # def discount_price(price, discount):
# #     def apply_discount():
# #         nonlocal price
# #         price = price*(1-discount)
# #         return price
# #     apply_discount()
# #     return price
# # def get_fullname(first_name, last_name, middle_name = ""):
# #     first_name = input(f'Vvedite first_name : ')
# #     last_name = input(f'Vvedite last_name : ')
# #     middle_name = input(f'Vvedite middle_name : ')
# #     if middle_name != "":
# #         return f'{first_name}, {last_name}, {middle_name}'
# #     else:
# #         return f'{first_name}, {last_name}' 

# # def get_fullname(first_name, last_name, middle_name = ""):
# #     if middle_name == "":
# #         return f'{first_name} {last_name}' 
# #     else:
# #         return f'{first_name} {middle_name} {last_name}'   

# # def format_string(string, length):
# #     if len(string) >= length:
# #         return string
# #     if len(string) < length:
# #         return string.append(((length - len(string)) // 2) * " ")         

             
# # def format_string(string, length):
# #     if len(string) < length:
# #         return " " * (length - len(string)) // 2 + string
# #     if len(string) >= length:
# #         return string
        
# # def factorial(n):
# #     if n < 2:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)


# # def number_of_groups(n, k):
# #     chislo_spiskov = factorial(n)/(factorial(n-k)*factorial(k))
# #     return int(chislo_spiskov)

# # a = int(input("chislo a :"))
# # # b = int(input("chislo b :"))
# # if b!=0:
# #     print(f'a\b = {a/b}')
# # else:
# #     print("divizion by zero")

#                                  #2 modul 1 leson + 2 lesson















#                                 #3 modul 1 lesons


# # from datetime import datetime

# # # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# # napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # # Поточна дата
# # current_date = datetime.now()

# # # Розрахунок кількості днів
# # days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# # print(days_since)

# # from datetime import datetime
# # import time

# # now = datetime.now()

# # # Форматування дати і часу
# # formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# # print(formatted_date) 

# # time.sleep(5)

# # # Форматування лише дати
# # formatted_date_only = now.strftime("%A, %d %B %Y")
# # print(formatted_date_only)

# # # Форматування лише часу
# # formatted_time_only = now.strftime("%I:%M %p")
# # print(formatted_time_only)  

# # # Форматування лише дати
# # formatted_date_only = now.strftime("%d.%m.%Y")
# # print(formatted_date_only)

# # from datetime import datetime

# # # Припустимо, у нас є дата у вигляді рядка
# # date_string = "2023.03.14"

# # # Перетворення рядка в об'єкт datetime
# # datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# # print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу
    
    
# # from datetime import datetime, timezone

# # local_now = datetime.now()
# # utc_now = datetime.now(timezone.utc)

# # print(local_now)
# # print(utc_now)  # Виведе поточний час в UTC

# # import time

# # # Записуємо час на початку виконання
# # start_time = time.perf_counter()

# # #  Виконуємо якусь операцію
# # for _ in range(1_000_000):
# #     pass  # Просто проходить цикл мільйон разів
# # time.sleep(5)
# # #  Записуємо час після виконання операції
# # end_time = time.perf_counter()

# # #  Розраховуємо та виводимо час виконання
# # execution_time = end_time - start_time
# # print(f"Час виконання: {execution_time} секунд")

# # import random
# # def kubik(a):
# # print(kubik(random.randint(1,6)))

# # import random

# # def kubik():
# #     dice_roll = random.randint(1, 6)
# #     print(f"Ви кинули {dice_roll}")
# # kubik()

#                                 ################################# From Code to Def ##############
# # import random

# # fruits = ['apple', 'banana', 'orange']
# # print(random.choice(fruits))
# #                                   #############################
# # import random

# # def cjo(fruits = ['apple', 'banana', 'orange']):
# #     return print(random.choice(fruits))
# # cjo()

#                                     #########################
# # import random

# # def asd(participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']):
# #     team = random.sample(participants, 4)
# #     return print(f"Команда: {team}")
# # asd()

# # def get_days_from_today(user_input = input("Input date: ")):
# #     date = datetime.strptime(user_input, "%Y-%M-%D")
# #     current_date = datetime.now()
# #     date1 = date - current_date
# # print(date1)    

#                             #  Функция для генерирования случайных чисел для лотереи
# # import random
# # list_with_lotery_digits = []                  
# # random_digit = random.randint(1, 100)

# # list_with_lotery_digits.extend(25)  
# # print(list_with_lotery_digits)    
# # import random                        
# # min = 5
# # max = 60
# # quantity = 6
# # list_with_lotery_digits = []
# # while quantity >= 1:   
# #     random_digit = random.randint(min, max)       
# #     list_with_lotery_digits.append(random_digit)
# #     print(list_with_lotery_digits)  
# #     quantity = quantity - 1          
# # print("Числа выходят из заданного диапазон\nМинимальное значение 1, максимальное 1000\nКолличество желаемых чисел не больше 1000 ")
# # import random
# # list_with_lotery_digits = [1,2,3,4,5,5,5,6,7,8]
# # for i in list_with_lotery_digits:
# #     random_number = random.randint(1, 6)
# #     if i != random_number:
# #         list_with_lotery_digits.append(random_number)
# # print(list_with_lotery_digits)
        
# # import random
# # list = [1,5,6,5,15,16,20,21,20,45,34]
# # for i in list:
# #     if i == i+1:
# #         list.remove[i]
# # print(list)

# # import random
# # def get_num(min, max, q):
# #     for i in [min, max, q]:
# #         if not (1<= i <= 1000):
# #             return []
# #         uq_num = random.sample(range(min, max +1), q)
# #         return sorted(uq_num)
# # lotery_num = get_num(55,50,5)
# # print(lotery_num)
 
# # import random
# # def get_numbers_ticket(min, max, quantity):                                   # СОЗДАЕМ ФУНКЦИЮ      
# #         if (min >= 1 and (min > max)) and (max <=1000) and (quantity <= max): # ПРОВЕРЯЕМ СООТВЕТСВУЮТ ЛИ ПАРАМЕТРЫ           
# #             list_with_lotery_digits = []                                      # СОЗДАЕМ ПУСТОЙ СПИСОК           
# #             while quantity >= 1:                                              # ЗАПУСКАЕМ ЦИКЛ С НУЖНЫМ КОЛЛИЧЕСТВОМ ПОВТОРЕНИЙ                                  
# #                 random_digit = random.randint(min, max)                       # ПОЛУЧАЕМ СЛУЧАЙНОЕ ЧИСЛО ИЗ ЗАДАНООГО ДИАПАЗОНА
# #                 if random_digit not in list_with_lotery_digits:               # ПРОВЕРЯЕМ ЧТО БЫ ЭТО ЧИСЛО УЖЕ НЕ БЫЛО В СПИСКЕ                        
# #                     list_with_lotery_digits.append(random_digit)              # ДОБАВЛЯЕМ ЧИСЛО В СПИСОК           
# #                     quantity = quantity - 1                                   # УМЕНШАЕМ ИТЕРАЦИЮ ЦИКЛА НА 1 (если число уже есть в списке,то итерация не уменшается)
# #                     return sorted(list_with_lotery_digits)                            # СОРТИРУЕМ СПИСОК И ВОЗВРАЩАЕМ В ФУНКЦИЮ   
# #         else:                                                                 # ВЫВОДИМ ПРЕДУПРЕЖДЕНИЕ ЕСЛИ ЗАДАННЫЕ АРГУМЕНТЫ НЕ СООТВЕТСВУЮТ ДИАПАЗОНУ
# #             print("Числа выходят из заданного диапазон\n\
# # Минимальное значение 1, максимальное 1000\n\
# # Колличество желаемых чисел не больше 1000 ")   
# # print(get_numbers_ticket(10, 500, 4))
            
# # import re

# # text = "Моя електронна адреса: example@example.com"
# # pattern = r"\w+@\w+\.\w+"
# # match = re.search(pattern, text)

# # if match:
# #     print("Електронна адреса:", match.group())

#                    #ФУНКЦИЯ ДЛЯ ПРИВЕДЕНИЯ ТЕЛ.НОМЕРОФ В НУЖНЫЙ ФОРМАТ
# import re
# def normalize_phone(phone_number):                                  # СОЗДАЕМ ФУНКЦИЮ
#     pattern = r"[\+\d+]"                                            # СОЗДАЕМ ПАТЕРН (ищем + и все цифры)
#     normalize_phone = re.findall(pattern, phone_number)             # ПРИМЕНЯЕМ ПАТЕРН (удаляя при этом все остальное)     
#     if len(normalize_phone) == 12:                                  # ПРОВЕРЯЕМ ДЛИННУ ЧТО БЫ ПОНЯТЬ КАКИХ ЗНАКОВ НЕ ХВАТАЕТ
#         normalize_phone.insert(0, '+')                              # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
#     elif len(normalize_phone) == 11:                                #
#         normalize_phone.insert(0, '+3')                             # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
#     elif len(normalize_phone) == 10:                                #
#         normalize_phone.insert(0, '+38')                            # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
#     elif 10 < len(normalize_phone) > 13:                            # ПРОВЕРКА ВАЛИДНОСТИ ВХОДНЫХ ДАННЫХ (не могу придумать как обработать, если будет +80979940862)
#         print("В номере недостаточно цифр\nНеверный формат данных")
#         return []                                                   # СООБЩАЕМ ОБ ОШИБКЕ ЕСЛИ ДАННЫЕ НЕ ВАЛИДНЫ  
#     normalize_phone = "".join(normalize_phone)                      # ОБЪЕДЕНЯЕМ
#     return normalize_phone                                          # ВОЗВРАЩАЕМ В ФУНКЦИЮ НУЖНЫЙ ФОРМАТ ТЕЛ.НОМЕРА

# print(normalize_phone(" -  -  0тт97-99-4 0-862")

# import datetime as dt                            
# from datetime import datetime as dtdt 
# from datetime import timedelta as td              
# users = [                                              
#     {"name": "John Doe", "birthday": "1985.01.2"},
#     {"name": "Jane Smith", "birthday": "1990.12.31"}
# ]

# # def get_upcoming_birthdays():                                                  
# congratulation_data = []          #что сюда запхнуть формат???                    
# today = dtdt.today().date()                  #today().date()                                              
# fday = today + td(days = 7)
# print(fday)
# for user in users:                                               
#     bu = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() 
#     bu = dt.date(today.year,bu.month, bu.day )
#     if today < bu <= (today + td(days=7)):
#         print(bu)
# import datetime as dt                            
# from datetime import datetime as dtdt 
# from datetime import timedelta as td              
# users = [                                              
#     {"name": "John Doe", "birthday": "1985.01.28"},
#     {"name": "Jane Smith", "birthday": "1990.01.29"}
# ]    
# congratulation_data = []
# dict = {}                                 
# today = dtdt.today().date()                                                 
# fday = today + td(days = 7)
# for user in users:                                               
#     bu = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() 
#     bu = dt.date(today.year,bu.month, bu.day ) 
#     if (today < bu) and (bu <= fday):
#         if bu.weekday == 5:
#             bu = bu + td(days = bu.days +2)    
#         elif bu.weekday == 6:
#             bu = bu + td(days = +1)             
#         dict["name"] = user.get("name")
#         dict["congratulation_date"] = bu
#         congratulation_data.append(dict)      
# print(congratulation_data)                

# bdate=("1985.12.29")
# bdate=dtdt.strptime(bdate, "%Y.%m.%d").date()
# print(bdate)
# a = bdate.weekday()  
# print(a)                            
# bdate = bdate + td(days = 2)  
# # print(bdate)



                                        # 4 module 


# byte_str = 'some text'.encode()
# print(byte_str)

# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел   

# for num in [127, 255, 1156]:
#   print(hex(num))

# s = "Привіт!"

# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

#from pathlib import Path

# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 