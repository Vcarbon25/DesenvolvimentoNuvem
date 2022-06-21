from ast import Pass
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
            global VOC, VOP
            #vetor ombro->cotovelo = cotovelo -ombro
            VOC = np.add(ArCot,MOmbro)
            #vetor ombro->punho = punho-ombro
            VOP = np.add(ArPunho,MOmbro)
            ROP=np.multiply(VOP,VOP) #raiz ombro punho, o array agora é os elementos da soma
            ROC = np.multiply(VOC,VOC) #raiz ombro cotovelo array elementos da soma 
            DOC = np.sqrt(ROC.sum()) #distancia ombro cotovelo
            DOP = np.sqrt(ROP.sum()) #dist ombro punho
            print('Ombro cotovelo: ',DOC)
            print('Ombro-punho: ',DOP)
            salvar(VOC,VOP)
        else:
            print("Refazer Calibração")
    else:
        print('Refazer Calibração')
salvou=0
def salvar(Vomcot,Vompu, Pombro, Pcotovelo, Ppunho):
    global salvou
    salvou +=salvou
    #end = "C:\Users\SAMSUNG\Documents\Faculdade\TCC Federal\MedidasRealizadas"
    arquivo = open("Medidas.txt","a")
    txtsalvou=str(salvou)
    txtVOC = str(Vomcot)
    txtVOP=str(Vompu)
    parte1 = "leitura N"+txtsalvou+"ponto ombro: "+Pombro+" Cotovelo "+Pcotovelo+" Punho "+Ppunho
    parte2 = " VOC: "+txtVOC+" VOP: "+txtVOP+"\n"
    texto = parte1+parte2
    arquivo.write(texto)
    arquivo.close()

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
        try:
            cord_cot=[results.pose_landmarks.landmark[11].x,results.pose_landmarks.landmark[11].y,results.pose_landmarks.landmark[11].z]
            cord_pun=[results.pose_landmarks.landmark[15].x,results.pose_landmarks.landmark[15].y,results.pose_landmarks.landmark[15].z]
            print("punho: ",cord_pun,"\ncotov: ",cord_cot)
        except:
            pass    
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
    