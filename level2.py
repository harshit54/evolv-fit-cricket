import cv2
import sys
import tensorflow as tf

model = tf.keras.models.load_model('evolvfit-challenge-model')

player_names = [ 
    'Bhuvneshwar Kumar',
    'Dinesh Karthik',
    'Hardik Pandya',
    'Jasprit Bumrah',
    'K. L. Rahul',
    'Kedar Jadhav',
    'Kuldeep Yadav',
    'Mohammed Shami',
    'MS Dhoni',
    'Ravindra Jadeja',
    'Rohit Sharma',
    'Shikhar Dhawan',
    'Vijay Shankar',
    'Virat Kohli',
    'Yuzvendra Chahal']

model.summary()

import numpy as np
from PIL import Image
# cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    

    image = Image.fromarray(frame, 'RGB').resize((150,150))

    # image = tf.keras.preprocessing.image.load_img(image, target_size=(150, 150))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch.
    predictions = model.predict(input_arr)
    predictions = np.squeeze(predictions)

    name = player_names[np.argmax(predictions)]

    coordinates = (150,400)
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (255,0,255)
    thickness = 2
    frame = cv2.putText(frame, name, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Text", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()