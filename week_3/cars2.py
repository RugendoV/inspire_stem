# this is a class describing cars
# by Rugendo

class car:
    def _init_ (self,model, make, yoprod, fuel_cap , color , horsepower):
        self.model = model 
        self.make = make 
        self.yoprod = yoprod 
        self.fuel_cap = fuel_cap
        self.color = color 
        self.horsepower = horsepower 

    def print_make(self,make) :
        print("The car is of {0} make".format(self.make))  

    def set_make(self,make):
        self.make = make 

    def get_make(self):
        return self.make


my_car = car("Defender ","Toyota", "2016","2500 cc" ,"lilac","3900hp")

friends_car = car("Impalla ","Chrevolet", "1969","2500 cc" ,"lilac","3900hp")

my_car.print_make("Chrevolet") 


my_car.set_make("Ford")
friends_car.set_make("Toyota")

print(my_car.get_make())
print(friends_car.get_make())









