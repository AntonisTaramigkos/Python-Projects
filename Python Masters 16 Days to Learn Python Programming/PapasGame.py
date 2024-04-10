# 
from random import shuffle
import os


game_list =["O","X","O"]

def cl_screen():
    os.system('cls')

def shuffle_list(list):
  #shuffle the list 
  shuffle(list)
  return list


def guess_player():
  
    new_list = shuffle_list(game_list)
    print(new_list)

    while True:
    
        guess = int(input("Δίαλεξε μια απο τις τρείς θέσεις 1,2,3 η πατα 0 για έξοδο :"))

        # if guess == 1 and new_list[0] == "X" :
        #     print("To βρήκες!!!")
        #     print(new_list)
        #     break
        
        # elif guess == 2 and new_list[1] == "X" :
        #     print("To βρήκες!!!")
        #     print(new_list)
        #     break
        
        # elif guess == 3 and new_list[2] == "X" :
        #     print("To βρήκες!!!")
        #     print(new_list)
        #     break
        # elif guess == 0:
        #     print("Σε περιμένω να ξαναπαίξουμε!!")
        #     exit()
        # else:
        #     print("Δεν ειναι εδώ!!")
        #     pass
        if new_list[guess-1] == "X":
            print("To βρήκες!!!")
            print(new_list)
        elif guess == 0:
            print("Σε περιμένω να ξαναπαίξουμε!!")
            exit()
        else:
            print("Δεν ειναι εδώ!!")
        
            


cl_screen()
print("Εδω΄ειναι ο Παπάς!")
print(game_list)
print("Πρόσεχε καλά ανακατέω τις καρτες!!")
print("Που ειναι τώρα ο Παπάς???")


guess_player()