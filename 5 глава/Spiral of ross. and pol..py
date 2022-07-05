# Спираль из розеток и многоугольников (неудачно!) :( P.s. уже удачно
import turtle
t = turtle.Pen ()
turtle.bgcolor ("black")
colors = ["red", "yellow", "blue", "green", "purple",
          "white", "pink", "gray", "orange", "brown"]
sides = int(turtle.numinput("Количество сторон",
                            "Сколько сторон будет у вашей спирали?"))
for m in range (5,75):
    t.left(360 / sides + 5)
    t.width (m//25+1)
    t.penup()
    t.forward (m*4)
    t.pendown()
    t.pencolor(colors[m%sides])
    if (m % 2 == 0):
        for n in range (sides):
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range (sides):
            t.forward(m)
            t.right(360/sides)