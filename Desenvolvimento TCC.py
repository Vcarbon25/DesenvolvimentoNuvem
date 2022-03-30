import cv2 #biblioteca necessária para o uso da camera

cap = cv2.VideoCapture(0) #aqui o argumento da função será o indice da câmera utilizada

while True: #esse loop nao pode ser interrompido
    sucess, frame = cap.read() #desempacotamento dos dados

    cv2.imshow("camera", frame) #abre um popout com a imagem enviada,e o titulo escolhido
    if cv2.waitKey(10)&0xFF == ord('q'):  #observa se determinada tecla foi pressionada para executar,no caso q
        break
cap.close()     #fecha a imagem da camera
cv2.destroyAllWindows()     #fecha a janela de display