                        #  ФУНКЦИЯ ВОЗВРАЩАЕТ КОЛ-ВО ДНЕЙ ОТ ВВЕДЕННОЙ ДАТЫ К СЕГОДНЯШНЕЙ

from datetime import datetime                                           # ИМПОРТИРУЕМ datetime из datetime
def get_days_from_today():                                              # СОЗДАЕМ ФУНКЦИЮ
    try:                                                                # НАЧАЛО БЛОКА ОБРАБОТКИ ОШИБОК
        user_input = input("Введите дату в формате ГГГГ-ММ-ДД : ")      # ВВЕДЕНИЕ ДАТЫ ПОЛЬЗОВАТЕЛЕМ
        user_data = datetime.strptime(user_input, '%Y-%m-%d')           # ПРИВЕДЕНИЕ В ОБЪЕКТ datetime 
        curent_date = datetime.now()                                    # ПОЛУЧАЕМ СЕГОДНЯШНЮЮ ДАТУ
        quantity_days = curent_date - user_data                         # ВЫЧИСЛЯЕМ РАЗНИЦУ МЕЖДУ ВВЕДЕННОЙ И СЕГОДНЯШНЕЙ ДАТОЙ    
        return quantity_days.days                                       # ВОЗВРАЩАЕМ В ФУНКЦИЮ РАЗНИЦУ ТОЛЬКО В ДНЯХ  
    except Exception:                                                   # КОНЕЦ БЛОКА ОБРАБОТКИ ОШИБОК НЕВЕРНОГО ВВОДА ДАННЫХ
        print("Дата введена в неверном формате или даты не существует") # СООБЩАЕМ ОБ ОШИБКЕ
print(get_days_from_today())                                            # ВЫЗЫВАЕМ ФУНКЦИЮ И ПРОВЕРЯЕМ, КАКИЕ ДАННЫЕ ВОЗВРАЩАЕТ