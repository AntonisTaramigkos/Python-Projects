# class Cow:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(self.name + " moos")

# class Sheep:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(self.name + " bleats")

# cow1 =Cow("Mandy")
# sheep1 = Sheep("Cloud")

# cow1.talk()
# sheep1.talk()


# def animal_talks(animal):
#     animal.talk()
# # for animal in animals:
# #     animal.talk()


# class Wizard():
#     def attack(self):
#         print("magic attack")

# class Archer():
#     def attack(self):
#         print("shoot arrow")

# class Samurai():
#     def attack(self):
#         print("katana attack")
        
# characters = [Archer, Wizard, Samurai]

# for char in characters:
#     char.attack()

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return(f'"{self.title}", from {self.author}')
    
    def __del__(self):
        print(f"Book {self.title} deleted")

my_book = Book("Lord of the rings", "J.R. Tolkien", 1000)
print(my_book)
del my_book
    