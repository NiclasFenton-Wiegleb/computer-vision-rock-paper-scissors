#from keras.models import load_model
import cv2

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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

#The code below creates a preview window and video capture loop

#vc = cv2.VideoCapture(0)

#while True:
    # Capture the video frame by frame
#    ret, frame = vc.read()
    #Display the resulting frame
#    cv2.imshow('frame', frame)
    #the 'q' button is set as the quitting button
#    if cv2.waitKey(1) and OxFF == ord('q'):
#        break

#After the loop release the captured object
#vid.release()
#Destroy all windows
#cv2.destroyAllWindows()


#model = load_model('keras_model.h5')


#def get_prediction(vc):
    #predictions = model.predict_classes(vc, verbose =1)
    #return predictions