# Problem :- Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla", "Model S1", "90kWh")
print(my_tesla.full_name())
print(my_tesla.get_brand())
