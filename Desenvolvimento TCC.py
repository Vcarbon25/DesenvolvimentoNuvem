import cv2 #biblioteca necessária para o uso da camera

cap = cv2.VideoCapture(0) #aqui o argumento da função será o indice da câmera utilizada

while True: #esse loop nao pode ser interrompido
    sucess, frame = cap.read() #desempacotamento dos dados

    cv2.imshow("camera", frame) #abre um popout com a imagem enviada,e o titulo escolhido
    cv2.waitKey(1)