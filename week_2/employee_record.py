# This is a program to determine employees salaries and bonuses
# Date : 21/2/24
# Name : Victoria Rugendo

employee_name : input("Enter the employee's name: ") # type: ignore
salary : int(input("Enter the employee's salary :")) # type: ignore
bonuses : float(input("Enter the employee's bonuses : ")) # type: ignore
p = 1.3
b = 0.95

newSalary = p * salary
newBonuses = b * bonuses

print("The employee's name is",employee_name)
print("The above employee's salary is",salary)
print("The above employee recieves bonuses worth ",bonuses)
print("The employee's new salary is",newSalary)
print("The employee's new bonuses are",newBonuses)


