import cv2
from cv2 import COLOR_RGB2BGR #biblioteca necessária para o uso da camera
import mediapipe as mp #bibliotecapara a detecção da postura

#prepara as ferramentas para chamada facil
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0) #aqui o argumento da função será o indice da câmera utilizada
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic: #determina as especificações e o simbolo do modelo holistico utilizado
    while cap.isOpened(): #loop enquanto camera aberta
        sucess, frame = cap.read() #desempacotamento dos dados
        #cv2 entrega uma imagem em BGR mas o processamento é em RGB
        imagemRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(imagemRGB)  #processamento da imagem
        #recolorir novamente para BGR para desenhar e colocar em tela
        imagemBGR = cv2.cvtColor(imagemRGB, COLOR_RGB2BGR)
        #desenho das posições na imagem atual
        mp_drawing.draw_landmarks(imagemBGR, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(100,255,100),thickness=4,circle_radius=6),
        mp_drawing.DrawingSpec(color=(100,100,255),thickness=3,circle_radius=5))
        cv2.imshow("Detecção de POSE", imagemBGR) #abre um popout com a imagem enviada,e o titulo escolhido
        if cv2.waitKey(10)&0xFF == ord('n'):
            x = results.pose_world_landmarks.landmark[0].x
            y = results.pose_world_landmarks.landmark[0].y
            z = results.pose_world_landmarks.landmark[0].z
            print("Coordenadas do nariz: (",x,",",y,",",z,")")
            #inserindo outro comando
        if cv2.waitKey(10)&0xFF == ord('p'):
            print('entrou na analise')
            jex = results.pose_world_landmarks.landmark[25].x
            jey = results.pose_world_landmarks.landmark[25].y
            qex = results.pose_world_landmarks.landmark[23].x
            qey = results.pose_world_landmarks.landmark[23].y
            jdx = results.pose_world_landmarks.landmark[26].x
            jdy = results.pose_world_landmarks.landmark[26].y
            qdx = results.pose_world_landmarks.landmark[24].x
            qdy = results.pose_world_landmarks.landmark[24].y
            Dados = {'qex':qex,'qey':qey,'qdx':qdx,'qdy':qdy,'jex':jex,'jey':jey,'jdx':jdx,'jdy':jdy}
            print ('dicionario de postura:',Dados)


        if cv2.waitKey(10)&0xFF == 27:  #fecha Com ESC
            break
cap.release()     #fecha a imagem da camera
cv2.destroyAllWindows()     #fecha a janela de display
#reconectado
#2 ola