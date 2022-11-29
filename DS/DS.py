#!/usr/bin/python3
class stack:
    def __init__(self):
        self.elements = ""
        self.length = 0     
    
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    
    def push(self,new_element):
        if self.is_empty() == False:
            self.elements += ","
            self.length += 1
        self.elements += new_element
        self.length += 1
        return self.elements
    
    def pop(self):
        self.elements = self.elements[:self.__len__()-2]
    
    def __len__(self):
        return self.length
    
    def __str__(self):
        return self.elements