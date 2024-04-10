#Class
class Bird:

    wings = True


    def __init__(self, color, species):
        self.color = color
        self.species = species
        
    def chirp(self):
        print(f"peep, i am {self.color}")

    def fly(self,feets):
        print(f"The bird is flying {feets} feets high")
    
    def paint_black(self):
        self.color = "black"
        print(f"The bird is now {self.color}")
    
    @classmethod
    def lay_eggs(cls,number):
        print(f"It laid {number} eggs")


my_bird = Bird("black", "Tucan")
another_bird =Bird("red", "Parot")
tweetie = Bird("Yellow","Canarine")
tweetie.chirp()

print(f"My bird is {my_bird.species} and it is {my_bird.color}")
print(my_bird.wings)

tweetie.paint_black()
Bird.fly("450")