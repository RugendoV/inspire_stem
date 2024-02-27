# the multiplication table
# Date : 22/2/24
# Name : Victoria Rugendo


num = int(input("Multiplication table of:"))
for n in range (1,11) : 
    print (num, 'x' , n ,'=' num * n  ) # type = error 


# entire table
    
for col in range (1-10):
    for rows in range (1-10):
        print(rows * col , end = '\t')