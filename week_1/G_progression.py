# This is a program to determine the solutions to geometric progressions
# Date : 20/2/24
# Name : Victoria Rugendo

s = float(input("Enter the first term"))
r = float(input("Enter the common ratio"))
b = float(input("Enter the number of the term"))

p = s * (r**(b-1))

print("The answer to the geometric progression is ",p )
