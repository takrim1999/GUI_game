#!/usr/bin/python3
import turtle
import random

class Turtles:
    def __init__(self,name="Give name",color="red",x=0,y=0,shape="turtle"):
        self.name = name
        self.color = color
        self.shape = shape
        self.x = x
        self.y = y
    def initialize(self):
        new = turtle.Turtle()
        new.penup()
        new.shape(self.shape)
        new.color(self.color)
        new.setpos(self.x,self.y)
    def run(self):
        # new = self.new
        for i in range(100):
            new.forward(1)
        
    def __str__(self):
        return "My name is {}".format(self.name)

def main():
    turtle.Screen()
    red = Turtles(name="Red Turtle",color="red",x=-200,y=0)
    blue = Turtles(name="Blue Turtle",color="blue",x=-200,y=-200)
    green = Turtles(name="Green Turtle",color="green",x=-200,y=200)
    red.initialize()
    red.run()
    
    
    turtle.done()

main()