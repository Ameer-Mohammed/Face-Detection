import cv2
import numpy as np

# Load the Haar Cascade classifier for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(img):

    if img is None:
        return None

    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(img, 1.3, 5)
    if len(faces) == 0:
        return img

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 122, 222), 2)
    return img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = detect_faces(frame)
    if frame is None:
        break

    cv2.imshow('Video Face detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()