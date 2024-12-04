# Problem :- Create an ElectricCar class that inherits from the car class and has an additional attribute battery_size.

class car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S1", "90kWh")
print(my_tesla.full_name())