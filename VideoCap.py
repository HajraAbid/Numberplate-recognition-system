import cv2


numPlate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture(0)



while True:

    _, img = cap.read()
    detect = numPlate_cascade.detectMultiScale(img, 1.01, 50)

    for (x, y, w, h) in detect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('image', img)

    if cv2.waitKey(33) == 27:
        break

cap.release()