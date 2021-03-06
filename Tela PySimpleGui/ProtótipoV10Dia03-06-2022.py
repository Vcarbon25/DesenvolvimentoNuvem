import cv2
import PySimpleGUI as sg
import mediapipe as mp
import math

def Listar_cameras():
    index=0
    lista=[]
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            cap.release()
            break
        else:
            lista.append(index)
        cap.release()
        index+=1
    return lista

def Geometria_Analitica(ombro, cotovelo,punho):
    #etapa print
    #print('Coordenadas ombro (',ombro.x,',',ombro.y,',',ombro.z,')')
    Cord_ombro=[ombro.x,ombro.y,ombro.z]
    Cord_cotovelo = [cotovelo.x,cotovelo.y,cotovelo.z]
    Cord_punho = [punho.x,punho.y,punho.z]
    Shouder_wrist = math.sqrt((Cord_ombro[0]-Cord_punho[0])^2+(Cord_ombro[1]-Cord_punho[1])^2+(Cord_ombro[2]-Cord_punho[2])^2)
    Shoulder_Elbow = math.sqrt((Cord_ombro[0]-Cord_cotovelo[0])^2+(Cord_ombro[1]-Cord_cotovelo[1])^2+(Cord_ombro[2]-Cord_cotovelo[2])^2)
    #Shouder_wrist = math.dist(Cord_ombro,Cord_punho)
    #Shoulder_Elbow = math.dist(Cord_ombro,Cord_cotovelo)
    
    print('distancia ombro-cotovelo: ',Shoulder_Elbow)
    print('Distancia ombro_punho: ',Shouder_wrist)
    if Shoulder_Elbow <Shouder_wrist:
        print('Angulo de abertura maior que 90°')
    elif Shoulder_Elbow>Shouder_wrist:
        print('Angulo de abertura menor que 90°')
    else:
        print('Caiu no Limbo')

#definir a tela
cameras=Listar_cameras()
Exames = ['Camera Simples','Angulo Corporal']

linha1 = [[sg.Image(filename="",key="camera")]]
linha2 = [sg.Text('Camera: '),sg.OptionMenu(cameras,default_value=' Cam ',key='CamSel'),sg.Button('Realizar Medida')]
linha3=[sg.Text('Exibir: '),sg.OptionMenu(Exames,default_value='Tipo',key='ImgSel'),sg.Button('Interromper')]
linha4=[sg.Text('Resultados: '),sg.Output(size=(40,4))]
layout=[linha1,linha2,linha3,linha4]
janela=sg.Window('V10DoTCC Mediapipe ',layout).finalize()


cap = cv2.VideoCapture(0)       # Setup the camera as a capture device
mp_drawing = mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic
while True:                     # The PSG “Event Loop”

    event, values = janela.Read(timeout=20, timeout_key='timeout')      # get events for the window with 20ms max wait
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        sucess, frame = cap.read()
        imagemRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = holistic.process(imagemRGB)#obtem os resultados do mediapipe
        #imagemBGR = cv2.cvtColor(imagemRGB,cv2.COLOR_RGB2BGR) #se ficar muito lento delete essa linha e use frame para desenhar
        mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(100,255,100),thickness=4,circle_radius=6),mp_drawing.DrawingSpec(color=(100,100,255),thickness=3,circle_radius=5))
        janela['camera'].Update(data=cv2.imencode('.png', frame)[1].tobytes()) # Update image in window
    if event == 'Realizar Medida':
        try:
            Geometria_Analitica(results.pose_landmarks.landmark[11],results.pose_landmarks.landmark[13],results.pose_landmarks.landmark[15])
        except:
            pass
    if event==sg.WINDOW_CLOSED:
        cap.release()
        break