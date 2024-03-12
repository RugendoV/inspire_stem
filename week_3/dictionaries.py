#
# 
# 28/2/24

laptop = {"make":"hp","color":"black","weight":"1.2kg","year":"2021"}

print(laptop["make"])
print(laptop["color"])
print(laptop["year"])

laptop["color"] = "red"
laptop["year"] = "2009"

laptop["size"] = "1200mm * 600mm"

del laptop["color"]
print(laptop)

s_lap = laptop.copy
print(laptop)


'''
for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
'''