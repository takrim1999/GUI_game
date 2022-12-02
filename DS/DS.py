#!/usr/bin/python3
# class stack:
#     def __init__(self):
#         self.elements = ""
#         self.length = 0     
    
#     def is_empty(self):
#         if self.length == 0:
#             return True
#         else:
#             return False
    
#     def push(self,new_element):
#         if self.is_empty() == False:
#             self.elements += ","
#             self.length += 1
#         self.elements += new_element
#         self.length += 1
#         return self.elements
    
#     def pop(self):
#         self.elements = self.elements[:self.__len__()-2]
    
#     def __len__(self):
#         return self.length
    
#     def __str__(self):
#         return self.elements

class Stack:
    def __init__(self,size=8):
        self.size = size
        self.i = 0
        self.array = [None]*size

    def is_empty(self):
        if self.i == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.i+1==self.size:
            return True

    def push(self,element):
        if self.is_full():
            print("stack overflowed")
        else:
            self.array[self.i] = element
            self.i+=1

    def pop(self):
        self.array[self.i]=None
        self.i-=1
    def __str__(self):
        j = 0
        while j<self.i:
            print(self.array[j],end="")
            j+=1
        return ""

ds = Stack()
print(ds.is_empty())
print(ds)
ds.push(5)
print(ds.is_empty())
print(ds)
ds.push(6)
print(ds.is_empty())
print(ds)
ds.pop()
print(ds.is_empty())
print(ds)
ds.push(5)
ds.push(5)
ds.push(5)
ds.push(5)
ds.push(5)
ds.push(5)
ds.push(5)
print(ds)