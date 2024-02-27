# Program to give salary increment
# Name : Victoria Rugendo
# Date : 27/02/24

s =int(input("Enter your salary:"))

if  s >= 100000:                 # type : ignore
    s_inc = 1.3 * s
elif s>= 100000 and s<=150000 :             
    s_inc = 1.15 * s
else :
    s_inc = 1.05 * s 

print("Your new salary is:",s_inc)