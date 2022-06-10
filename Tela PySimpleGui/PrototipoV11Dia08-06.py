import cv2
import PySimpleGUI as sg
import mediapipe as mp
import math
import numpy as np
import time

RelacaoCalibrada = 0

def Geometria_Analitica(comp ,ombro, cotovelo,punho):
    #etapa print
    #print('Coordenadas ombro (',ombro.x,',',ombro.y,',',ombro.z,')')
    ArOmbro=np.array([ombro.x,ombro.y,ombro.z])
    ArCot = np.array([cotovelo.x,cotovelo.y,cotovelo.z])
    ArPunho = np.array([punho.x,punho.y,punho.z])
    MOmbro = np.multiply(ArOmbro,-1)
    dif = np.add(ArCot,MOmbro)
    quad=np.multiply(dif,dif)
    DistAtual = np.sqrt(quad.sum())
    RelacaoAtual = DistAtual/comp
    print(RelacaoAtual)
    global RelacaoCalibrada
    if RelacaoAtual>0.9*RelacaoCalibrada:
        if RelacaoAtual<1.1*RelacaoCalibrada:
            print ("medida válida")
            
        else:
            print("Refazer Calibração")
    else:
        print('Refazer Calibração')
    

def Calibracao(comp, ombro, cotovelo):
    print("rotina de calibração")
    ArOmbro = np.array([ombro.x,ombro.y,ombro.z])
    ArCot = np.array([cotovelo.x,cotovelo.y,cotovelo.z])
    MOmbro = np.multiply(ArOmbro,-1)
    dif = np.add(ArCot,MOmbro)
    quad=np.multiply(dif,dif)
    DistTela = np.sqrt(quad.sum())
    global RelacaoCalibrada
    RelacaoCalibrada = DistTela/comp
    print("Relação Calibrada: ",RelacaoCalibrada)

#definir a tela

linha1 = [[sg.Image(filename="",key="camera")]]
linha2 = [sg.Button('Calibrar Sistema'), sg.Button('Realizar Medida')]
linha3=[sg.Text("comp ombro-cotovelo esquerdo"),sg.Input(key='comprimento',size=(6,1)),  sg.Text('Verificação de Angulos corporais ')]
linha4=[sg.Text('Resultados: '),sg.Output(size=(40,6))]
layout=[linha1,linha2,linha3,linha4]
janela=sg.Window('V11DoTCC Mediapipe simplificado',layout).finalize()


cap = cv2.VideoCapture(0)       # Setup the camera as a capture device
mp_drawing = mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic
ptime=0
ctime=0
while True:                     # The PSG “Event Loop”

    event, values = janela.Read(timeout=20, timeout_key='timeout')      # get events for the window with 20ms max wait
    with mp_holistic.Holistic(min_detection_confidence=0.6, min_tracking_confidence=0.6) as holistic:
        sucess, frame = cap.read()
        imagemRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = holistic.process(imagemRGB)#obtem os resultados do mediapipe
        #imagemBGR = cv2.cvtColor(imagemRGB,cv2.COLOR_RGB2BGR) #se ficar muito lento delete essa linha e use frame para desenhar
        mp_drawing.draw_landmarks(frame,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(100,255,100),thickness=4,circle_radius=6),mp_drawing.DrawingSpec(color=(100,100,255),thickness=3,circle_radius=5))
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        nfps=int(fps)
        txtfps=str(nfps)
        cv2.putText(frame,txtfps,(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,50,150),3)
        janela['camera'].Update(data=cv2.imencode('.png', frame)[1].tobytes()) # Update image in window
        print(results.pose_landmarks.landmark[15])#vai imprimir constantemente a posução da mão esquerda para saber os valores da tela tirar depois
    if event == 'Calibrar Sistema':
        try:
            compinformado = float(values['comprimento'])
            Calibracao(compinformado, results.pose_landmarks.landmark[11],results.pose_landmarks.landmark[13])
        except:
            print('erro, o valor informado deve ser um número')
    if event == 'Realizar Medida':
        try:
            Geometria_Analitica(compinformado, results.pose_landmarks.landmark[11],results.pose_landmarks.landmark[13],results.pose_landmarks.landmark[15])
        except:
            pass
    if event==sg.WINDOW_CLOSED:
        cap.release()
        break