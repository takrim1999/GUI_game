#!/usr/bin/python3
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def diff(a,b):
    return abs(a-b)
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Zero Division Error"
    else:
        return a/b

def calculator(a=10,b=5,operation=sum):
    return operation(a,b)

print(calculator(100,5,div))