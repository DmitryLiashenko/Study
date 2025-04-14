"""пока не допилил классы в 7 ДЗ представлю код для сериализации и десериализации отдельно"""

import pickle

class AdressBook(dict):
        def save_data(book, filename="addressbook.pkl"):
            with open(filename, "wb") as f:
                pickle.dump(book, f)

        def load_data(filename="addressbook.pkl"):
            try:
                with open(filename, "rb") as f:
                    return pickle.load(f)
            except FileNotFoundError:
                    book = AdressBook()
                    return book

        

'''in main() function добавляем методы save_data и load_data'''

def main():
    book = AdressBook.load_data("addressbook.pkl")
    while True: 
        command = "close"
        if command in ["close", "exit"]:                     # БЛОК ВЫХОДА ИЗ БОТА
            print("Good bye!")
            AdressBook.save_data(book)
            break 