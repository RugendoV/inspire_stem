#
#
#

friends = ["Sam","Lorna","Kate","Stan","Aldrin","Wesley"]

for friend in friends :
    print(friend)

enemies = friends[:] # to copy one list to another

print(enemies)

fruits = ("guava","mango","apples","grapes","oranges","jackfruit")
# to slice the list to get a part of the list

print(fruits[0:3])

print(fruits)

squares = []   # initializes an empty list

for x in range (0,11) :
    squares.append(x**2)
print(squares)
