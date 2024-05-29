from turtle import *
import random

donatello = Turtle()
donatello.shape("arrow")
donatello.color("black")


colormode(255)

def draw_shape(sides):
    angle = 360 / sides
    for x in range(0,sides):
        donatello.forward(75)
        donatello.left(angle)

for n in range (3, 100):
    R = random.randrange(0,256)
    G = random.randrange(0,256)
    B = random.randrange(0,256)

    donatello.color(R, G, B)
    draw_shape(n)
    

screen = Screen()
screen.colormode()
screen.exitonclick()