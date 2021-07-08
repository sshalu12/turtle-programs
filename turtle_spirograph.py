from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
t1 = Turtle()
t1.speed("fastest")


def random_numbers():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colorr = (r, g, b)
    return colorr


def spiro(gap):
    for i in range(int(360/gap)):
        t1.circle(100)
        t1.setheading(t1.heading()-gap)
        # t1.right(5)
        t1.color(random_numbers())


spiro(5)
s = Screen()
s.exitonclick()
