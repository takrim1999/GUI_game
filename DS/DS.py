#!/usr/bin/python3
class stack:
    def __init__(self,elements):
        self.elements = elements    
    def push(self,new_element):
        self.elements += new_element
        return self.elements
    def pop(self):
        self.elements = self.elements[:self.__len__()-1]
    def __len__(self):
        count = 0
        for i in self.elements:
            count+=1
        return count
    def __str__(self):
        return self.elements

new = stack("12345")
print(new)
new.pop()
print(new)