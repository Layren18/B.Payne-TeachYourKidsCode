import turtle
t = turtle.Pen ()
turtle.bgcolor ("black")
colors = ["red", "yellow", "blue", "green", "purple",
          "white", "pink", "gray", "orange", "brown"]
family = []
name = turtle.textinput('Моя семья',
                        'Введите любое имя или "Стоп", чтобы выйти:')
while name!= "Стоп":
    family.append(name)
    name = turtle.textinput('Моя семья', 'Введите ещё одно имя или "Стоп", чтобы выйти:')
for x in range (100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font=("Arial",
                                         int((x+4)/4), "bold"))
    t.left(360/len(family)+2)