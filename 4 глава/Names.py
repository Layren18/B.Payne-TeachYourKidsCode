name = input ("Как тебя зовут?")
while name!= "Стоп":
    for x in range(100):
        print(name, end = " ")
    print ()
    name = input ('Введите ещё одно имя или введите слово "Стоп", чтобы выйти:')
print("Спасибо за игру!")