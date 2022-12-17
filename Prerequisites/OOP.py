class student:
    def __init__(self,name="Students Name",age="18",height=152):
        self.name = name
        self.age = age
        self.height = height
    def talk(self):
        print(f"{self.name} is Talking")
    def study(self):
        print(f"{self.name} is Studying")
    def __str__(self):
        return f"I am {self.name} I am {self.age} years old and my height is {self.height}"
    
class exam(student):
    def study(self):
        return super().study()
        # print(f"{self.name} is not styding nor sleeping")
