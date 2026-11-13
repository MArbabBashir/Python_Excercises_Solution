print("======= Exercise 11: Coffee Machine with Multi-Resource Tracking =======")

class CoffeeMashine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_coffee(self)->bool:
        water = 200
        coffee = 20
        milk = 150
        if self.water >= water and self.coffee >= coffee and self.milk >= milk:
            self.water -= water
            self.coffee -= coffee
            self.milk -= milk
            return True

        else:
            return False
coffee_mashine_1 = CoffeeMashine(1000, 60, 300)
res = coffee_mashine_1.make_coffee()
print(res)
res = coffee_mashine_1.make_coffee()
print(res)
res = coffee_mashine_1.make_coffee()

print(res)

print("======= Exercise 12: Shared Class Attribute Across Instances =======")
class Vehicle:
    def __init__(self,name:str, color='white', max_speed:int=200):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        print(f"{self.name} - Color: {self.color} , Max Speed: {self.max_speed}")
v1 = Vehicle('Tesla')
v2 = Vehicle('BMW','red', 250)


print("======= Exercise 13: Bus Subclass Inheriting from Vehicle =======")
class Vehicle:
    def __init__(self,name:str, max_speed):
        self.name = name
        self.max_speed = max_speed
    def display(self):
        print(f"{self.name} - Max Speed: {self.max_speed}")
class Bus(Vehicle):
        pass

bus1 = Bus("School Bus", "120Km/h")
bus1.display()

print("======= Exercise 14: override Parent Method Using super() =======")
class Vehicle:
    def __init__ (self, name:str):
        self.name = name
    def seating_capacity(self, capacity:int):
        print(f"{self.name} - Seating Capacity is: {capacity}")
class Bus(Vehicle):
    def seating_capacity(self):
        super().seating_capacity(50)
bus1 = Bus("School Bus")
print("=======  Exercise 15: Add Maintenance Fee in Child Class via super() =======")
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare * 0.10

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

taxi = Taxi(500)
print("Total fare with maintenance fee:", taxi.total_fare())

print("=======   Polymorphism with Dog & Cat speak() =======")
class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self, sound: str='i can speak but...'):
        self.sound = sound
        print(f"{self.name} - says: {self.sound}")

class Dog(Animal):
    def speak(self, sound:str):
        self.sound = sound
        super().speak(self.sound)
class Cat(Animal):
    def speak(self, sound:str):
        self.sound = sound
        super().speak(self.sound)

cat_1 = Cat("kitty")
cat_1.speak("Meow meow")
dog_1 = Dog("Tommy")
dog_1.speak("baoh baoh")

