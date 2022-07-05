# Калейдоскоп
import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "purple",
          "white", "pink", "gray", "orange", "brown"]
for i in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    t.penup() # 1 спираль
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup() # 2 спираль
    t.setpos(-x, y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.left(91)
    t.penup() # 3 спираль
    t.setpos(-x, -y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.left(91)
    t.penup() # 4 спираль
    t.setpos(x, -y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.left(91)