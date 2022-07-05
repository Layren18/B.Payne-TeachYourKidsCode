# Хотите спираль?
import turtle
t = turtle.Pen ()
t.width (2) #ширина
answer = input ("Хотите увидеть спираль? Введите \"Да\" чтобы увидеть спираль")
if answer == 'Да' or answer == 'да':
    print ("Работаем...")
    for x in range (100):
        t.forward(x*2)
        t.left(89)
print("Ну вот, готово!\nСпасибо за помощь в развитии моих навыков программирования! =D")