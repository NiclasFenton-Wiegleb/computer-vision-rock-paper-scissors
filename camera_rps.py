from keras.models import load_model
import cv2
import numpy as np
from PIL import Image
import time

#Initiate trained model
model = load_model('keras_model.h5', compile=False)

def get_prediction(video_input):
    # Getting prediction array from model
    predictions_arr = model.predict(video_input, verbose =1)
    #Flattening array and converting to list
    predictions_flat = predictions_arr.flatten()
    predictions_lst = predictions_flat.tolist()

    # Getting index of most likely class and assigning corresponding value as
    # predicted play.
    prediction_index = predictions_lst.index(predictions_flat.max())
    plays = ['Rock', 'Paper', 'Scissors', 'Nothing']
    predicted_play = plays[prediction_index]
    print(predicted_play)
    return predicted_play

def get_prediction_from_vid():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while(True):
        
        # Capture the video frame by frame
        ret, frame = vid.read()

        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')
        #Resizing into dimensions you used while training
        im = im.resize((224,224))
        img_array = np.array(im)

        #Expand dimensions to match the 4D Tensor shape.
        img_array = np.expand_dims(img_array, axis=0)

        #Call function to get prediction from model
        prediction = get_prediction(img_array)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def timer():
    #Initiatlises the start time
    start_time = int(time.time())

    while True:
        #Current time variable is refreshed with each loop
        current_time = int(time.time())
        seconds = current_time - start_time
        if seconds <= 3:
            print(seconds)
        else:
            break

timer()


