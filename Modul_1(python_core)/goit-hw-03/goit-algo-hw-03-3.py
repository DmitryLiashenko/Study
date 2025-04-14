                   #ФУНКЦИЯ ДЛЯ ПРИВЕДЕНИЯ ТЕЛ.НОМЕРОФ В НУЖНЫЙ ФОРМАТ
import re
def normalize_phone(phone_number):                                  # СОЗДАЕМ ФУНКЦИЮ
    pattern = r"[\+\d+]"                                            # СОЗДАЕМ ПАТЕРН (ищем + и все цифры)
    normalize_phone = re.findall(pattern, phone_number)             # ПРИМЕНЯЕМ ПАТЕРН (удаляя при этом все остальное)     
    if len(normalize_phone) == 12:                                  # ПРОВЕРЯЕМ ДЛИННУ ЧТО БЫ ПОНЯТЬ КАКИХ ЗНАКОВ НЕ ХВАТАЕТ
        normalize_phone.insert(0, '+')                              # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
    elif len(normalize_phone) == 11:                                #
        normalize_phone.insert(0, '+3')                             # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
    elif len(normalize_phone) == 10:                                #
        normalize_phone.insert(0, '+38')                            # ДОБАВЛЯЕМ НЕДОСТОЮЩЕЕ
    elif 10 < len(normalize_phone) > 13:                            # ПРОВЕРКА ВАЛИДНОСТИ ВХОДНЫХ ДАННЫХ (не могу придумать как обработать, если будет +80979940862)
        print("В номере недостаточно цифр\nНеверный формат данных")
        return []                                                   # СООБЩАЕМ ОБ ОШИБКЕ ЕСЛИ ДАННЫЕ НЕ ВАЛИДНЫ  
    normalize_phone = "".join(normalize_phone)                      # ОБЪЕДЕНЯЕМ
    return normalize_phone                                          # ВОЗВРАЩАЕМ В ФУНКЦИЮ НУЖНЫЙ ФОРМАТ ТЕЛ.НОМЕРА

print(normalize_phone("     0503451234"))