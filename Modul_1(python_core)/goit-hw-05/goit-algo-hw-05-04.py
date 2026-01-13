                               # ФУНКЦИИ ДЛЯ РАБОТЫ ОСНОВНОГО КОДА

def input_error(func):                              # ФУНКЦИЯ-ДЕКОРАТОР ДЛЯ ВВЕДЕННЫХ КОМАНД
    def inner(*args, **kwargs):                     # ФУНКЦИЯ ОБРАБОТКИ ОШИБОК
        try:                                        # НАЧАЛО БЛОКА ОШИБОК
            return func(*args, **kwargs)            # ПРОБУЕМ
        except ValueError:                          # ЕСЛИ ОДНА ИЗ ОШИБОК ВОЗНИКАЕТ 
            return "Give me name and phone please." # 
        except IndexError:                          #
            return "No found"                       #
        except KeyError:                            #
            return "No soch name found"             # ВОЗВРАЩАЕМ В ФУНКЦИЮ СООБЩЕНИЕ ОБ ОПРЕДЕЛЕННОЙ ОШИБКЕ
    return inner                                    # ВОЗВРАЩАЕМ В ДЕКОРАТОР ФУНКЦИЮ ОБРАБОТКИ ОШИБОК

@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def parse_input(user_input):            # ФУНКЦИЯ ПАРСЕРА КОМАНД           
    cmd, *args = user_input.split()     # РАЗДЕЛЯЕМ ВВОД НА КОМАНДУ И АРГУМЕНТЫ
    cmd = cmd.strip().lower()           # ПРИВОДИМ В НИЖНИЙ РЕГИСТР И УДАЛЯЕМ ЛИШНИИ ПРОБЕЛЫ КОМАНДЫ
    return cmd, *args                   # ВОЗВРАЩАЕМ КОМАНДУ И СПИСОК АРГУМЕНТОВ

@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def add_contact(args, contacts):        # ФУНКЦИЯ ДОБАВЛЕНИЯ КОНТАКТОВ
    name, phone = args                  # ПРИСВАИВАЕМ АРГУМЕНТЫ ИМЕНИ И ТЕЛЕФОНУ
    contacts[name] = phone              # ЗАНОСИМ В СЛОВАРЬ ПО КЛЮЧЮ ТЕЛЕФОН
    return "Contact added."  
            
@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def change_contact(args, contacts):     # ФУНКЦИЯ ИЗМЕНЕНИЯ КОНТАКТА
    name, phone = args
    for key, value in contacts.items(): # ИТЕРИРУЕМСЯ ПО СЛОВАРЮ
        if key == name:                 # ЕСЛИ КЛЮЧ СОВПАДАЕТ С ИМЕНЕМ 
            contacts[name] = phone      # ПРИСВАИВАЕМ ИМЕНИ НОВЫЙ ТЕЛЕФОН
    return "Contact change"

@input_error                            # ПРИМЕНЯЕМ ДЕКОРАТОР
def show_phone(args, contacts):         # ФУНКЦИЯ ПОКАЗЫВАЕТ ТЕЛЕФОН ПО ИМЕНИ
    name = args
    for key, value in contacts.items(): # ИТЕРИРУЕМСЯ ПО СЛОВАРЮ
        if name == key:                 
            return contacts[key]        # ВОЗВРАЩАЕМ ЗНАЧЕНИЕ НАЙДЕНОЕ ПО КЛЮЧУ
        else:
            return "No found"           # ВОЗВРАЩАЕМ НЕ НАЙДЕНО ЕСЛИ ИМЕНИ НЕТ В КОНТАКАХ

def show_all(contacts=None):
    s = ''                                         # ОБЪЯВЛЯЕМ ПУСТУЮ СТРОКУ s
    for key in contacts:                           # ИТЕРИРУЕМ СЛОВАРЬ
        s+=(f"{key:10} : {contacts[key]:10}\n")    # ФУНКЦИЯ ВЫВОДИТ ВСЕ КОНТАКТЫ В СЛОВАРЕ(ДОБАВИТЬ \n)(странная реализация \n)
    return s                                       # ВОЗВРАЩАЕМ СЛОВАРЬ В ФУНКЦИЮ


def main():                                        # ОСНОВНАЯ ФУНКЦИЯ 
    contacts = {}                                  # СОЗДВЕМ ПУСТОЙ СЛОВАРЬ
    print("Welcome to the assistant bot!")         # ПРИВЕТСТВИЕ
    while True:                                    # ЗАПУСКАЕМ ЦИКЛ
        user_input = input("Enter a command: ")    # ПОЛУЧАЕМ КОМАНДУ
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:           # БЛОК ВЫХОДА ИЗ БОТА
            print("Good bye!")
            break 
        elif command == "hello":                   # БЛОК ЗАПРОСА КОМАНДЫ
            print("How can I help you?")
        elif command == "add":                     # ДОБАВЛЕНИЕ КОНТАКТА
            print(add_contact(args, contacts))     # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "change":                  # СМЕНА КОНТАКТА
             print(change_contact(args, contacts)) # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "phone":                   # ПОКАЗЫВАЕТ КОНТАКТ ПО ИМЕНИ
            print(show_phone(args[0], contacts))   # ПЕРЕДАЕМ ФУНКЦИИ АРГУМЕНТЫ И СЛОВАРЬ
        elif command == "all":                     # ПОКАЗЫВВАЕМ ВЕСЬ СЛОВАРЬ
            print(show_all(contacts))              # ПЕРЕДАЕМ ФУНКЦИИ СЛОВАРЬ
        else:                                      
            print("Invalid command.")              # СООБЩАЕМ О НЕ ПРАВИЛЬНОЙ КОМАНДЕ

if __name__ == "__main__":                         # ПРОВЕРКА ЗАПУЩЕННА ЛИ ГЛАВНЫЙ КОД, А НЕ МОДУЛЬ
    main()
