class Pet:
    no_of_pets : int =0     #   CLass attribute common to all objects 

    def __init__(self, name: str, age: int):  
        print("Inside Init")
        Pet.no_of_pets += 1
        self.name = name             
        self.age = age

    def print(self):
        print(f"Pet Name -> {self.name}")
        print(f"Pet Age -> {self.age}")

    def speak(self):
        print("Dont know what to say")

    @classmethod
    def whoamI(cls):
        return cls.no_of_pets

class Dog (Pet):
    def speak(self):
        print("I Bark")

class Cat (Pet):

    def __init__(self, name, age, color : str):
        super().__init__(name, age)         # Invoke constructor of parent
        self.color=color

    def speak(self):
        print("I Meow")

    def print(self):
            print(f"Pet Name -> {self.name}")
            print(f"Pet Age -> {self.age}")
            print(f"Pet Color -> {self.color}")

class Fish(Pet):
    pass

pet_one = Dog("Doggie", 9)
pet_one.speak()
pet_one.print()
print(pet_one.no_of_pets)
print(Pet.no_of_pets)

pet_two = Cat("Cattie", 3, "Brown")
pet_two.speak()
pet_two.print()
print(pet_one.no_of_pets)
print(Pet.no_of_pets)

pet_three = Fish("Goldie", 3)
pet_three.speak()
pet_three.print()
print(pet_one.no_of_pets)
print(Pet.no_of_pets)

print(Pet.whoamI())