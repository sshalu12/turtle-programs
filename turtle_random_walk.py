from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

directions = [0, 90, 180, 270, 360]

t1 = Turtle()
t1.pensize(15)
t1.speed("normal")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rr = (r, g, b)
    return rr


for i in range(200):

    t1.setheading(random.choice(directions))
    t1.color(random_color())
    t1.forward(30)

s1 = Screen()
s1.exitonclick()
