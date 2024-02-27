# gets sum of first 20 numbers
# Name : Rugendo
# Date : 26/02/24

sum_nums = 0
max_val = int(input("Enter the maximum number:"))

for x in range(0,max_val+1):
    sum_nums = sum_nums + x 
    print("The sum of the numbers is",sum_nums)