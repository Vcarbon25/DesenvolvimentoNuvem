import cv2

cap = cv2.VideoCapture(0) #argumento é o indice da camera utilizada
while cap.isOpened(): #Fica em Loop enquanto a janela aberta
    sucess, img = cap.read()

    cv2.imshow('Camera',img)
    if cv2.waitKey(10)&0xFF == 27:  #fecha Com ESC
            break
cap.release()     #fecha a imagem da camera
cv2.destroyAllWindows()     #fecha a janela de display
