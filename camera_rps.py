'''
This code creates a class to play Rock, Paper Scissors with the computer via 
the webcam.

The camera_rps class containse the functions get_computer_choice(), which
generates a random choice or Rock, Paper Scissors as the computer's play. There is
also a timer(seconds) function, which delays the code by as many seconds as
are passed into the function without stopping the code.

The get_prediction(image_array) takes a frame captured by the camera and passes it
to the trained keras model to predict what the user is most likely playing.

Finally, the play function runs through a loop where it counts to 3, captures a frame,
predicts the play the user is showing the camera, generates the computer choice and
keeps score of who wins. The first player to win 3 rounds wins the game.

To improve the accuracy of the image recognition, 20 frames are taken and run through
the model. The predicted classes are added to a list and the most common element
is chosen as the user's choice.

This improved accuracy from _____ when taking only a single frame to ___ when taking
20 and picking the most common.


'''

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

class camera_rps:

    def __init__(self):
        pass
    # This function generates the computer's choice by selecting a random index between 0 and 2 and returning the play with the corresponding index
    def get_computer_choice(self):
        choices_list = ['rock', 'paper', 'scissors']
        choice_index = random.randint(0,2)
        computer_choice = choices_list[choice_index]
        return computer_choice

    #Counts to the number of seconds passed into the function.
    def timer(self, count_to):
        #Initiatlises the start time
        start_time = int(time.time())

        while True:
            #Current time variable is refreshed with each loop
            current_time = int(time.time())
            seconds = current_time - start_time
            if seconds <= count_to:
                continue
            else:
                break
            
    #Uses the loaded keras model to predict the play the user is showing the camera.
    def get_prediction(self, video_input):

        # Getting prediction array from model
        predictions_arr = model.predict(video_input)
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


    # Play the game by accessing camera
    def play(self):
        # define a video capture object
        vid = cv2.VideoCapture(0)

        #Assigning variables to track computer and user wins.
        computer_wins = 0
        user_wins = 0

        while True:
                #Wait for 3 seconds
            print("Countdown:")
            for val in range(3):
                self.timer(1)
                print(val+1)

            #get user choice
            user_choice_list = []
            for val in range(20):
                # Capture the video frame by frame
                ret, frame = vid.read()

                #Convert the captured frame into RGB
                im = Image.fromarray(frame, 'RGB')
                #Resizing into dimensions you used while training
                im = im.resize((224,224))
                img_array = np.array(im)

                #Expand dimensions to match the 4D Tensor shape
                img_array = np.expand_dims(img_array, axis=0)

                # Display the resulting frame
                cv2.imshow('frame', frame)

                #Call function to get prediction from model
                user_choice = self.get_prediction(img_array)
                user_choice_list.append(user_choice)

            #Select the most common element in user_choice_list
            user_choice = max(set(user_choice_list), key=user_choice_list.count)
            print(f"User: {user_choice}")
            #Pick computer play
            computer_choice = self.get_computer_choice()
            print(f"Computer: {computer_choice}")
                
            #check if prediction is anything other than 'nothing' class
            if user_choice != 'nothing':
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
            else:
                continue
            print(f"Computer wins: {computer_wins}")
            print(f"Your wins: {user_wins}")

            #break loop once a player has three victories.
            if computer_wins == 3 or user_wins == 3:
                if user_wins > computer_wins:
                    print('You won!')
                    break
                else:
                    print('You lost')
                    break
            #When 'q' key hit break loop
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        vid.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

player = camera_rps()
player.play()