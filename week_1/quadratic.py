#program to solve the quadratic equation
# Date : 20/02/24
# Name : Victoria Rugendo


import math

a = float(input("enter the coefficient of 1st term :"))
b = float(input("enter coefficient of 2nd term : "))
c = float(input("enter the constant : "))


d = ((b)**2) - 4 * (a) * (c)

x_1 = (-b + math.sqrt(d) ) / (2 * a) 
x_2 = (-b + math.sqrt(d) ) / (2 * a )

print("The solution to the quadratic equation is :", x_1)
print("The solution to the quadratic equation is :", x_2)
