import turtle
t = turtle.Pen ()
turtle.bgcolor ("black")
num = int(turtle.numinput("Количество окружностей",
                          "Сколько окружностей вы хотите увидеть?"))
for x in range (num) :
    t.pencolor ("white")
    t.circle(100)  # 100 - радиус
    t.left(360/num)  # 360 градусов разделенное на число, введённое пользователем