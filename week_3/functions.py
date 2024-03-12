# functions: a block of code running together as a unit
'''
for example sum(10,20) is to add two numbers
sum--->is to initialize the function or define the function
(10,20) is to call the function
'''

def print_name():
    print("My name is Victoria")

# calling the function
print_name()


def print_details(name , age , id , gender):
    print("I am {0} , {1} years old . My id number is {2} and my gender is {3} ".format(name,age,id,gender))


print_details("Victoria" , "18" , "793316451", "female")
print_details("Victor" , "31" , "29383121", "male")


# the sum of some numbers
def sum_nums(x,y) :
    return x + y     # return inarudisha the final answer

z = sum_nums(10,20)
print(z)

# product of numbers
def prod_nums(x,y) :
    return x*y 

print(prod_nums(5,6))

# for loop
def print_odds(first_no, last_no) :
    for i in range(first_no,last_no) :
        print(i % 2)

print_odds(0,15)