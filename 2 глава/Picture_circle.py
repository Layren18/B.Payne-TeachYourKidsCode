import turtle 
t=turtle.Pen ()
turtle.bgcolor ("black")
colors = ["red", "green", "blue", "yellow", "purple",
          "white", "pink", "gray"]
sides = int(turtle.numinput ("Сколько сторон?",
                          "Сколько сторон вы хотите (от 1 до 8)", 4, 1, 8))
for x in range (100) :
    t.pencolor(colors[x % sides])
    t.circle (x * 3 / sides + x)
    t.left (360 / sides + 1)
    t.width (x * sides / 200)