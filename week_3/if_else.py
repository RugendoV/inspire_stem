# if else and what not


age = 17
if age > 18.1 :
    print("You are allowed to drive")

salary = 45000
if salary >30000 and salary < 50000 :   # and is used to add conditions 
    salary = (salary * 0.1) + salary 
    print(salary)


h_county = "Nyeri"

if h_county =="Nyeri" or h_county== "Meru":        # the two equals are meant to be there so that it works
    print("You get a bursary")


grade = 70

if grade >= 84 and grade <= 90 :
    print("You win a calculator")
elif grade >= 50 and grade<=83 :             # elif is a short way of saying if else
    print("You win a set")
else :
    print("You win nothing !!!")