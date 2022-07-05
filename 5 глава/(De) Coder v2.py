# Кодировщик - декодер версия 2
message = input("Введите сообщение для кодирования "
                "или раскодирования (на АНГЛИЙСКОМ языке):")
key = eval(input("Введите кол-во символов, на сколько "
                 "позиций требуется передвинуть букву в сообщении (1-25):"))
message = message.upper()
output = " "
for letter in message:
    if letter.isupper():
        value = ord(letter) + key
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("Выходное сообщение:", output)