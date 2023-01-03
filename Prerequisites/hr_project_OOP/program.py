#!/usr/bin/python3
import hr
import disgruntled

salary_employee = hr.SalaryEmployee(1,"John Doe",1500)
hourly_employee = hr.HourlyEmployee(2,"Jane Taylor",15,20)
commision_employee = hr.CommisionEmployees(3,"Rojer Beakon",2000,50)
disgruntled_employee = disgruntled.DisgruntledEmployee(28,"Zuckerberg")
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([salary_employee,hourly_employee,commision_employee,disgruntled_employee])