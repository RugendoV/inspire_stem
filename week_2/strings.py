#
#
#

city ="Nairobi"

print(city[0]) # N
print(city[1]) # a
print(city[2]) # i
print(city[3]) # r
print(city[4]) # o
print(city[5]) # b
print(city[6]) # i

print(city[-2]) # this one has neg so it reverses the order of the characters
# convert to upper case


print(city)
print("\n\n") # prints a new line
print(city.upper())

name = "VICTORIA"
print(name)
print(name.lower()) # converts strings to lower case

town = "            Naivasha         "

print(town)
print("\t") #new tab
print(town.strip())    # strip removes empty spaces

# add two strings

f_name = "Joyce"
s_name = "aketh"

full_name =f_name + s_name 

print(full_name)


# replacing a character in a string

fruit = "orangeoooooo"

print(fruit.replace('o','y')) #to replace something

subject = "Physical: Sciences"
print(subject.split(":")) # prints the two words separately 

age = 30
height = 1.58 
print("I am {0} years old and {1} metres tall ".format(age,height))   # hii inaweka vitu ndani ya curly brackets


activity = "dancing"
print("My hobby is %s" %(activity))     # %s is to show a string

# printing a float
height = 1.3454885412
print("My height is %5.3f"% (height))

# printing an integer
age = 32
print("My age is %d"% (age)) 



name = "Victoria R"
print(len(name))

print(f"My full name is {name}")


school = " Engineering"
course = "Electrical"

print("I am studying {course} in the school of {school}".format(course="med",school="Human sciences"))



