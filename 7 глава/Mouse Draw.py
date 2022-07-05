# Рисование мышкой
import turtle
t = turtle.Pen ()
t.speed(0)
turtle.onscreenclick(t.setpos)
turtle.bgcolor("black")
t.pencolor("blue")
t.width(25)