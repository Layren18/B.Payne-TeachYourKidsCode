# Что нарисовать? Розетку или Многоугольник? Сколько будет сторон или окружностей?
import turtle
t = turtle.Pen ()
turtle.bgcolor ("black")
number = int(turtle.numinput("Количество сторон или окружностей",
                             "Сколько сторон или окружностей будет у фигуры?"))
shape = turtle.textinput("Какую фигуру вы хотите?",
                         "Введите \"Многоугольник\" или \"Розетка\"")
for x in range (number):
    if shape == 'Розетка':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
    t.pencolor("white")