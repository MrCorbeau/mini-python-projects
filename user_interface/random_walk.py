from turtle import *
import random

donatello = Turtle()

def random_color():
    colormode(255)

    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)

    return (R, G, B)

def walk(step, angle):
    rotation = random.randint(1,2)
    l_or_r = random.randint(0,1)
    if rotation == 1:
        donatello.forward(step)
        if l_or_r == 0:
            donatello.left(angle)
        else:
            donatello.right(angle)
    elif rotation == 2:
        donatello.backward(step)
        if l_or_r == 0:
            donatello.left(angle)
        else:
            donatello.right(angle)

for n in range (0,100):
    donatello.color(random_color())
    walk(random.randrange(0, 100, 25), random.randrange(0, 180, 15))

Screen().exitonclick()
