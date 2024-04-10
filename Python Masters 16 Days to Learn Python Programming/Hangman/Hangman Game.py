#The hug man game!
import random

# def player_lives():
life = 5
cpu_choice = []
hangman = []

def list_of_word():
    '''Here is a preconstracted list of words'''
    lst_of_words = ["apple", "man", "sunshine", "adventure", "chocolate", "laughter", "friendship"]
    return lst_of_words

def cpu_choose_word(lst):
    '''Cpu Choose a random world from the provided list'''
    global cpu_choice
    cpu_choice = list(random.choice(lst))
    print (cpu_choice)
    return cpu_choice
# cpu_choose_word(list_of_word())

def print_hangman():   
    '''Prints the underscores for each letter of the word'''
    global cpu_choice    
    print(("-") * (len(cpu_choice)))

     
def player_input():    
    '''Here player choose a letter an check if ia letter indeed'''
    while True:
        letter = input("Please select a letter: ")
        if not letter.isalpha(): #isalpha!
            print("It has to be a letter.")
        else:
            print(f"You chose {letter}.")
            return letter
        print(letter)

def print_the_letters():
    '''I ll make a list from the underscores .
    i ll take each index from players choise and ill change it
    with the letter'''
    global cpu_choice    
    print(("-") * (len("adventure")))
    finded_letters = list((("-") * (len("adventure"))))
    print(finded_letters)
    
    print_the_letters()



        

def game_logic(player_input, cpu_choice):
    '''here we will check if player input is inside the letter
    of the word cpu has choose.If not player lose a life!
    so we call global life and we have two args, player input and cpu word
    we run an if loop an the i have to find the indexes of the letter in the word if there are more than one
    and i have to print to  the def print_hangman(word)'''
    global life    
    # if player_input in cpu_choice:
    #     indices = []
    #     for index, char in enumerate(cpu_choice):
    #         if char == player_input:
    #             indices.append(index)
    #             print(indices)
    #     print("You have found a letter")
    # else:
    #     life -= 1
    #     print(f"There is no {player_input} in the word :(\nYou have {life} lives now)")

    if player_input in cpu_choice:
        indices = [index for index, char in enumerate(cpu_choice) if char == player_input] 
        print("indices =", indices)
        print("You have find a letter") 
        return indices      

    else:
        life -= 1
        print(f"There is no {player_input} at the word :(\n You have {life} lives now)")


cpu_world =cpu_choose_word(list_of_word()) #STORE your DEF to Variebles always!! Or you will take  the function objects themselves instead of their return values.
print_hangman()
players_input = player_input()

game_logic(players_input, cpu_world)