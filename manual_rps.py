import random

def get_computer_choice():
    choices_list = ['Rock', 'Paper', 'Scissors']
    choice_index = random.randint(0,2)
    choice = choices_list[choice_index]
    return choice



def get_user_choice():
    choices_list = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Please select what to play:\n")
        user_choice = str(user_choice).lower()
        if not user_choice in choices_list:
            print("That input is not valid. Please choose from rock, paper, scissors.")
        else:
            return user_choice
            break
    

get_user_choice()


