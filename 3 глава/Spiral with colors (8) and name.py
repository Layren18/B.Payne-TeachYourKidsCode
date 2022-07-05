import turtle
t = turtle.Pen ()
turtle.bgcolor ("black")
colors = ["red", "yellow", "blue", "green", "purple",
          "white", "pink", "gray"]
name = turtle.textinput("Введите своё имя",
                        "Как тебя зовут?")
sides = int(turtle.numinput ("Сколько сторон?",
                          "Сколько сторон спирали вы хотите (от 1 до 8)", 4, 1, 8))
for x in range (100) :
    t.pencolor(colors[x % sides])
    t.forward (x * 3 / sides + x)
    t.penup ()
    t.write(name, font= ("Arial", int((x + 4) / 4),
                         "bold"))
    t.left (360 / sides + 1)
    t.width (x * sides / 200)