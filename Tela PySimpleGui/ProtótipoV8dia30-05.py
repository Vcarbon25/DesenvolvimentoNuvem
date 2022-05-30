import cv2
import PySimpleGUI as sg
import mediapipe as mp

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

#definir a tela
cameras=Listar_cameras()
Exames = ['Camera Simples','Angulo Corporal']

linha1 = [[sg.Image(filename="",key="camera")]]
linha2 = [sg.Text('Camera: '),sg.OptionMenu(cameras,default_value=' Cam ',key='CamSel'),sg.Button('Iniciar Exame')]
linha3=[sg.Text('Exibir: '),sg.OptionMenu(Exames,default_value='Tipo',key='ImgSel'),sg.Button('Interromper')]
linha4=[sg.Text('Resultados: '),sg.Output(size=(40,4))]
layout=[linha1,linha2,linha3,linha4]
janela=sg.Window('V8DoTCC Mediapipe ',layout).finalize()


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
    if event==sg.WINDOW_CLOSED:
        break