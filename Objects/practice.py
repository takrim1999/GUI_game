#!/usr/bin/python3
class Human:
    Name = "Human Name"
    Age = 0
    Height = 0
    Weight = 0
    Sex = "None"
    def gym(self):
        if self.Sex=="Male" and self.Age<17:
            self.Height += 1
        elif self.Sex=="Female" and self.Age<15:
            self.Height += 1
        self.Weight -= 1
    def __str__(self):
        # print(f"Name is {self.Name} Age is {self.Age}Years Height is {self.Height}CM and Weight is {self.Weight}KG")
        return f"Name is {self.Name}\nAge is {self.Age} Years\nHeight is {self.Height} CM\nWeight is {self.Weight} KG"

class Weapon:
    Name = "Weapon Name"
    Type = "Weapon Type"
    
    def fire(self):
        if self.Type == "MG":
            print("TAT TAT TAT TAT TAT TAT TAT TAT TAT TAT")
        if self.Type == "SMG":
            print("TAT TAT TAT TAT TAT")
        if self.Type == "AR":
            print("DHI DHI")
        if self.Type == "SR":
            print("TIU")