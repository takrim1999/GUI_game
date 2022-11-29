#!/usr/bin/python3
import turtle
import random

class Turtles(turtle.Turtle):
    def __init__(self,name="Give name",color="red",x=0,y=0,shape="turtle"):
        self.name = name
        self.color = color
        self.shape = shape
        self.x = x
        self.y = y
        turtle.shape(self.shape)
        turtle.color(self.color)
        turtle.setpos(self.x,self.y)

        
    def __str__(self):
        return "My name is {}".format(self.name)

def main():
    turtle.Screen()
    turtle.penup()
    red = Turtles(name="Red Turtle",color="red",x=-200,y=0)
    blue = Turtles(name="Blue Turtle",color="blue",x=-200,y=-200)
    green = Turtles(name="Green Turtle",color="green",x=-200,y=200)
    turtle.done()

# print(red)
main()