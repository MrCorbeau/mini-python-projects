from turtle import *
import random

donatello = Turtle()
donatello.speed("fastest")

def random_color():
    colormode(255)

    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)

    return (R, G, B)

for x in range(0, 36):
    donatello.color(random_color())
    donatello.circle(100)
    donatello.left(10)
    



screen = Screen()
screen.exitonclick()