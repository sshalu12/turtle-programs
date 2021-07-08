from turtle import Turtle, Screen
import random

t1 = Turtle()

choices = ["navy", "green", "olive", "salmon", "purple",
           "magenta", "rebecca purple", "medium violet red"]


def draw(num):
    for i in range(num):
        angle = 360/num
        t1.forward(100)
        t1.right(angle)


for i in range(3, 11):
    draw(i)
    t1.color(random.choice(choices))


s1 = Screen()
s1.exitonclick()
