# Dice Game
import random
import os

def clear_screen():
    os.system("cls")

class Die():

    def __init__(self):
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value


class Player():

    def __init__(self, die, is_computer=False ):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
        pass 

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def incriment_counter(self):
        self._counter += 1

    def decriment_counter(self):
        self._counter -= 1
    
    def roll_die(self):
        return self._die.roll()

class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("="*23)
        print("🎲 Welcome to DiceGame 🎲")
        print("="*23)
        while True:
            self.play_round()
            #TODO :IMplement game over
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        print("----- New Round -----")
        input("🎲 Paste any key to roll the dice. 🎲")

        #Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #Show the Values
        print(f"Your die :{player_value}")
        print(f"Computer die :{computer_value}")

        #Determine winner and loser
        if player_value > computer_value:
            print("You won the round 😁👍")
            self.update_counters(winner=self._player, looser=self._computer)
        elif computer_value > player_value:
            print("Computer won this round!! Try again!😒")
            self.update_counters(winner=self._computer, looser=self._player)
        else:
            print("Its a tie!! 😎")

        # Show counters
        self.show_counters()
    
    def update_counters(self, winner, looser):
        winner.decriment_counter()
        looser.incriment_counter()

    def show_counters(self):
        print(f"Your counter is {self._player.counter}")
        print(f"Computer counter is {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False        

    def show_game_over(self,winner):
        if winner.is_computer:
            print("\n================")
            print(" GAME OVER ✨✨")
            print("================")
            print("The computer won the game! Sorry...\n😒😒😒😒 ")
        else:
            print("\n================")
            print(" GAME OVER ✨✨")
            print("================")
            print("The player won!!🎉🎉🎉  ")

# Create Instansies

human_die = Die()
computer_die = Die()

human_player = Player(human_die, is_computer=False )
computer_player = Player(computer_die, is_computer=True)
my_game = DiceGame(human_player, computer_player)

clear_screen()
my_game.play()
