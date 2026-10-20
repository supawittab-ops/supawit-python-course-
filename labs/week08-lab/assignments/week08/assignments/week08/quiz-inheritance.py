class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, Number of Doors: {self.number_of_doors}"


vehicle = Vehicle("Honda", "Wave", 2020)
print(vehicle.get_info())

car = Car("Toyota", "Camry", 2022, 4)
print(car.get_info())