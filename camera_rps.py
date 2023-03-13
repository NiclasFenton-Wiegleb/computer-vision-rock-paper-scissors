from keras.models import load_model
import cv2
import numpy as np
from PIL import Image
import time
import random

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

#Initiate trained model
model = load_model('keras_model.h5', compile=False)

#Assigning variables to track computer and user wins.
computer_wins = 0
user_wins = 0

# This function generates the computer's choice by selecting a random index between 0 and 2 and returning the play with the corresponding index
def get_computer_choice():
    choices_list = ['rock', 'paper', 'scissors']
    choice_index = random.randint(0,2)
    computer_choice = choices_list[choice_index]
    return computer_choice

#Counts to the number of seconds passed into the function.
def timer(count_to):
    #Initiatlises the start time
    start_time = int(time.time())

    while True:
        #Current time variable is refreshed with each loop
        current_time = int(time.time())
        seconds = current_time - start_time
        if seconds <= count_to:
            #print(seconds)
            continue
        else:
            break
        
#Uses the loaded keras model to predict the play the user is showing the camera.
def get_prediction(video_input):

    # Getting prediction array from model
    predictions_arr = model.predict(video_input, verbose =1)
    #Flattening array and converting to list
    predictions_flat = predictions_arr.flatten()
    predictions_lst = predictions_flat.tolist()

    # Getting index of most likely class and assigning corresponding value as
    # predicted play.
    prediction_index = predictions_lst.index(predictions_flat.max())
    plays = ['rock', 'paper', 'scissors', 'nothing']
    prediction = plays[prediction_index]
    prediction = prediction.lower()
    return prediction

def get_winner(user_choice, computer_choice):
    if (computer_choice == 'rock' or user_choice == 'rock') and (computer_choice == 'paper' or user_choice == 'paper'):
        if user_choice == 'paper':
            user_wins += 1
        else:
            computer_wins += 1
    elif (computer_choice == 'rock' or user_choice == 'rock') and (computer_choice == 'scissors' or user_choice == 'scissors'):
        if user_choice == 'rock':
            user_wins += 1
        else:
            computer_wins += 1
    elif (computer_choice == 'paper' or user_choice == 'paper') and (computer_choice == 'scissors' or user_choice == 'scissors'):
        if user_choice == 'scissors':
            user_wins += 1
        else:
            computer_wins += 1
    

#TO DO - function needs to display video; rearrange so timer is in get_prediction();
# maybe get_prediction_from_vid could feed into get_prediction outside while loop? Or separate function to display video?

##FIX: Why does the code work outside of function and not within?

def play_camera_rps():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while True:
            #Wait for 3 seconds
            print("Countdown:")
            print(1)
            timer(1)
            print(2)
            timer(1)
            print(3)
            timer(1)

            # Capture the video frame by frame
            ret, frame = vid.read()

            #Convert the captured frame into RGB
            im = Image.fromarray(frame, 'RGB')
            #Resizing into dimensions you used while training
            im = im.resize((224,224))
            img_array = np.array(im)

            #Expand dimensions to match the 4D Tensor shape.
            img_array = np.expand_dims(img_array, axis=0)

            # Display the resulting frame
            cv2.imshow('frame', frame)

            #Call function to get prediction from model
            user_choice = get_prediction(img_array)
            print(user_choice)

            #Pick computer play
            computer_choice = get_computer_choice()
            print(computer_choice)
            
            #check if prediction is anything other than 'nothing' class
            if user_choice != 'nothing':
                get_winner(user_choice, computer_choice)
            else:
                continue
            print(f"Computer wins: {computer_wins}")
            print(f"Your wins: {user_wins}")

            #break loop once a player has three victories.
            if (computer_wins or user_wins) == 3:
                if user_wins > computer_wins:
                    print('You won!')
                    break
                else:
                    print('You lost')
                    break
            # the 'q' button is set as the quitting button you may use any
            # desired button of your choice
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

play_camera_rps()