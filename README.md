# Computer Vision RPS

This project aims to train a machine learning model that can determine if a human player is playing rock, paper or scissors with a webcam as input. The goal is to create an algorithm that can play the game with a human contestant. Please see below for the technologies used:

- Tensorflow (Model trained via https://teachablemachine.withgoogle.com/)

- Python


## Milestone 1

- The machine learning model was trained to recognise four classes: Rock, Paper, Scissors and Nothing. The training set contained 1300 images, 300 for each possible play and 400 for the Nothing class

- The files containing the model were downloaded from Teachable Machine and uploaded to this repository.

- The required dependencies can be found in the requirements.txt

## Milestone 2

 - Creating python script that allows a user to play RPS with the computer by manually inputting their play:

    1. Writing the function get_computer_choice that will randomly pick the computers play from a list of choices.

```
        def get_computer_choice():
            choices_list = ['rock', 'paper', 'scissors']
            choice_index = random.randint(0,2)
            computer_choice = choices_list[choice_index]
            return computer_choice
```

    2. Another function called get_user_choice is added that asks the user to input their play and only accepts valid options.

```
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
```

    3. Finally, the get_winner function takes in the play from both the computer and user and determines who won or if there is a tie. A corresponding statement is then printed to the console. This function goes through the possible scenarios and adds 1 to the score for whoever played the winning game. Everything else will indicate there was a tie.

```
        def get_winner(computer_choice, user_choice):
            computer_choice = computer_choice.lower()
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
```

    4. To put the above together into a game, the play function generates the computer's play, asks the user for input and passes the two choices as parameters to the get_winner function.

```
        def play():
            computer_choice = get_computer_choice()
            user_choice = get_user_choice()
            print(f'The computer played {computer_choice}.')
            get_winner(computer_choice, user_choice)
```

