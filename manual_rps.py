'''This code allows a user to play Rock, Paper, Scissors manually with the computer by inputting their play and comparing it to a random choice by the computer'''

import random

# This function generates the computer's choice by selecting a random index between 0 and 2 and returning the play with the corresponding index
def get_computer_choice():
    choices_list = ['rock', 'paper', 'scissors']
    choice_index = random.randint(0,2)
    computer_choice = choices_list[choice_index]
    return computer_choice


#This function asks the user to input their play
def get_user_choice():
    choices_list = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Please select what to play:\n")
        user_choice = str(user_choice).lower()
        if not user_choice in choices_list:
            #If the user enters anything that isn't a valid play, this message is printed and the user is asked to enter their input again
            print("That input is not valid. Please choose from rock, paper, scissors.")
        else:
            return user_choice
            break
    

# This function determines who won or if there was a tie and prints the corresponding statement.
def get_winner(computer_choice, user_choice):
    print(f'The computer played {computer_choice}')
    computer_win = 0
    user_win = 0
    if (computer_choice == 'rock' or user_choice == 'rock') and (computer_choice == 'paper' or user_choice == 'paper'):
        if user_choice == 'paper':
            user_win += 1
        else:
            computer_win += 1
    elif (computer_choice == 'rock' or user_choice == 'rock') and (computer_choice == 'scissors' or user_choice == 'scissors'):
        if user_choice == 'rock':
            user_win += 1
        else:
            computer_win += 1
    elif (computer_choice == 'paper' or user_choice == 'paper') and (computer_choice == 'scissors' or user_choice == 'scissors'):
        if user_choice == 'scissors':
            user_win += 1
        else:
            computer_win += 1
    if user_win > computer_win:
        print('You won!')
    elif user_win == computer_win:
        print('It is a tie!')
    else:
        print('You lost')

get_winner(get_computer_choice(), get_user_choice())

    #if computer_choice == 'rock':
        #if user_choice == 'rock':
            #print('It is a tie!')
        #elif user_choice == 'paper':
            #print('You won!')
        #else:
            #print('You lost')
    #if computer_choice == 'paper':
        #if user_choice == 'rock':
            #print('You lost!')
        #elif user_choice == 'paper':
            #print('It is a tie!')
        #else:
            #print('You won!')
    #if computer_choice == 'scissors':
        #if user_choice == 'rock':
            #print('You won!')
        #elif user_choice == 'paper':
            #print('You lost')
        #else:
           # print('It is a tie!')



