#!/usr/bin/python3

from abc import ABC,abstractmethod

class PayrollSystem:

    def calculate_payroll(self,employees):
        self.employees = employees
        print("\nCalculating Payroll\n")
        for employee in self.employees:
            print(f"Payroll for {employee.name}({employee.id}) is:")
            print(f"    Amount {employee.calculate_payroll()}")
        print("\n")

class Employees(ABC):
    def __init__(self,id,name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

class SalaryEmployee(Employees):
    def __init__(self,id,name,weekly_salary):
        super().__init__(id,name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
 
class HourlyEmployee(Employees):
    def __init__(self, id, name, hours_worked,hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked

class CommisionEmployees(SalaryEmployee):
    def __init__(self, id, name, weekly_salary,commision):
        super().__init__(id, name, weekly_salary)
        self.commision = commision
    
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision