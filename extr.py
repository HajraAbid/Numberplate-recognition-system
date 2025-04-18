import cv2

# Load the cascade
plant_cascade = cv2.CascadeClassifier('C:\\Users\\UMER ABBAS\\Desktop\\accident\\cascade.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)


while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the plants
    plants = plant_cascade.detectMultiScale(img, 1.01, 50)
    # Draw the rectangle around each plant
    for (x, y, w, h) in plants:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    if  cv2.waitKey(33) == 27:
        break
# Release the VideoCapture object
cap.release()