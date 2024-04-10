# # #Inheritance
# class Animal:
#     def __init__(self, age, color):
#         self.age = age
#         self.color = color

#     def born(self):
#         print("This animal has been born")

#     def talk(self):
#         print("This animal makes a sound")

# class Bird(Animal):
#     def __init__(self, age, color, altitud):
#         super().__init__(age,color)
#         # self.age = age
#         # self.color = color
#         self.altitud = altitud

#     def talk(self):
#         print("Chirp")
#         # return super().talk()
#     def fly(self,feet):
#         print(f"This bird flies {feet} feet")


# tweetie = Bird(3, "yellow", 196)
# tweetie.

# myanimal = Animal(5, "Black")

class Vertebrate:
    vertebrate = True

class Bird(Vertebrate):
    has_peak = True
    def lay_eggs(self):
        print("laying eggs")

class Reptile(Vertebrate):
    poisonous = True

class Fish(Vertebrate):
    def swim(self):
        print("swimming")
    def lay_eggs(self):
        print("laying eggs")

class Mammal(Vertebrate):
    def walk(self):
        print("walking")
    def nurse(self):
        print("nursing pups")

class Platypus (Fish, Reptile, Bird, Mammal):
    pass
Platypus.

