import random

numer = "0123456789"
leters_small = "abcdefghijklmnopqrstuvwxyz"
leters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punct = "!#$%&*+-=?@^_"
rem = "il1Lo0O"
chars = ""

print("Привет Я создатель безопасных паролей")
print("Какое кол-во паролей нужно сгенерировать?")
how_meny_pass = int(input())
print("какая длинна пароля должна быть?")
long = int(input())


print("Включать ли цифры? Да или Нет")
cifri = input()
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
propisnie = input()
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?")
strochnie = input()
print("Включать ли символы !#$%&*+-=?@^_?")
simvoli = input()
print("Исключать ли не однозначные символы?")
remove = input()


def generate_password(long, chars):
    return "".join(random.choice(chars) for _ in range(long))

if cifri == "Да":
    chars += numer
if propisnie == "Да":
    chars += leters_big
if strochnie == "Да":
    chars += leters_small
if simvoli == "Да":
    chars += punct

if remove == "Да":
    for ch in rem:
        chars = chars.replace(ch, "")

ls = []
for i in range(how_meny_pass):
    ls.append(generate_password(long, chars))


for i in ls:
    print(i)
