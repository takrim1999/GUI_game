#!/usr/bin/python3
import turtle
import random
turtle.Screen().setup(width=0.75, height=0.8, startx=None, starty=None)
turtle.screensize(bg="green")
def finish_line(x=480,y=300,width=15,line_pair=10,line_length=30):
    line = turtle.Turtle()
    line.speed(0)
    line.width(width)
    line.penup()
    line.setpos(x,y)
    line.pendown()
    line.setheading(270)
    for i in range(line_pair):
        line.color("black")
        line.forward(line_length)
        line.color("white")
        line.forward(line_length)
    line.penup()
    line.setpos(x+width,y-line_pair*2*line_length)
    line.setheading(90)
    line.pendown()
    for i in range(line_pair):
        line.color("black")
        line.forward(line_length)
        line.color("white")
        line.forward(line_length)   
# def turtles():
#     for i in range


finish_line()

turtle.done()