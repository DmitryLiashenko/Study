def caesar_encrypt(text, shift=10):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ALPHABET = alphabet.upper()
    result = ""

    for ch in text:
        if ch in alphabet:  # строчная буква
            idx = alphabet.index(ch)
            result += alphabet[(idx + shift) % len(alphabet)]
        elif ch in ALPHABET:  # заглавная буква
            idx = ALPHABET.index(ch)
            result += ALPHABET[(idx + shift) % len(ALPHABET)]
        else:  # пробелы, запятые и т.д.
            result += ch

    return result


text = "Блажен, кто верует, тепло ему на свете!"
print(caesar_encrypt(text, 17))
