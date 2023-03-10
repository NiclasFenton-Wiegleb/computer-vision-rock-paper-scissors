from keras.models import load_model
import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(30) & 0xFF == ord('q'):
       break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

#Initiate trained model

model = load_model('keras_model.h5')

#TO DO: convert 
def get_prediction(vid):
    predictions = model.predict_classes(, verbose =1)
    return predictions