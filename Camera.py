import cv2

cap = cv2.VideoCapture(0) #argumento é o indice da camera utilizada
while True: #Fica em Loop Infinito sem interromper a menos que feche IDE
    sucess, img = cap.read()

    cv2.imshow('Camera',img)
    cv2.waitKey(1)