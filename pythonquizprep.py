class RefuelExceeded(Exception):
    def __init__(self, fuel_capacity, combined):
        super().__init__(f"Car's fuel capacity is only {fuel_capacity}, added fuel exceeded by {combined - fuel_capacity}")

class Car:
    def __init__(self, brand, model, year, fuel_capacity, wheel_count):
        self.brand = brand
        self.fuel_capacity = fuel_capacity
        self.wheel_count = wheel_count
        self.model = model
        self.year = year

    def refuel(self, add_fuel):
        combined = add_fuel + self.fuel_capacity
        if combined > self.fuel_capacity:
            raise RefuelExceeded(self.fuel_capacity, combined)
        else:
            self.fuel_capacity = combined
    
        
car1 = Car("Toyota", 100, 4)

try:
    car1.refuel(20)
except RefuelExceeded as e:
    print(e)

print(car1.fuel_capacity)

def createCar():
    brand = input("Brand? ")
    



user_choice = input("Create car? y/n: ")

if user_choice.lower() in ["yes", "y"]:
    createCar()

