from PySimpleGUI import PySimpleGUI as sg
import cv2
import time
import mediapipe as mp
sg.theme('SandyBeach')

def Listar_cameras():
    index=0
    lista = []
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
       
def CameraSimples():
    global CamIndex
    cap = cv2.VideoCapture(CamIndex)  
    sucess, img = cap.read()
    ColocaNaTela(img)
    cap.release()

mp_drawing=mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
def ModeloCorpo():
    global CamIndex
    cap = cv2.VideoCapture(CamIndex)
    global mp_drawing, mp_holistic
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        sucess, imagemBGR = cap.read()
        imagemRGB=cv2.cvtColor(imagemBGR,cv2.COLOR_BGR2RGB)
        results = holistic.process(imagemRGB)
        mp_drawing.draw_landmarks(imagemBGR, results.pose_landmarks,mp_holistic.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(100,255,100),thickness=2,circle_radius=3), mp_drawing.DrawingSpec(color=(100,100,255),thickness=4,circle_radius=6))
        ColocaNaTela(imagemBGR)

ptime=0
ctime=0
def ColocaNaTela(cv2img):
    global ptime, ctime
    ctime=time.time()
    fps=1/(ctime-ptime)
    nfps=int(fps)
    txtfps=str(nfps)
    cv2.putText(cv2img,txtfps,(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,50,100),3)
    ptime=ctime
    ImgTamanho = cv2.resize(cv2img, Tamanho_Imagem) #faz a imagem do tamanho do configurado pela tupla
    ImgTela = cv2.imencode(".png",ImgTamanho)[1].tobytes()
    principal["camera"].update(data=ImgTela)


HabilitarCamera=True
camera_Width=320
camera_heigth = 240
Tamanho_Imagem=(camera_Width,camera_heigth)
cameras = Listar_cameras()

Exames=['Camera Simples','Angulo Corporal']
coluna_esquerda = [[sg.Image(filename="",key="camera")],[sg.Output(30,4)]]
SelCamera=int()
ImgSel=str()
coluna_do_meio = [[],[sg.Text('Camera: '),sg.OptionMenu(cameras,default_value='cam',key='SelCamera')],
[sg.Text('Selecione O Exame :'), sg.OptionMenu(Exames,default_value='escolha',key='ImgSel')],
[sg.Button('Iniciar Exame'),sg.Button('Interromper')]]
coluna_direita=[sg.Text('Resultados: '),sg.Output(size=(15,4))]
layout =[coluna_esquerda,coluna_do_meio, coluna_direita]
principal = sg.Window('V5 do TCC',layout).finalize()

while True:
    eventos, valores = principal.read()
    # atualiza a janela de acordo com o que já foi requisitado
    CamIndex= int(valores['SelCamera'])
    if HabilitarCamera:
        escolha = valores['ImgSel']
        if escolha == 'Camera Simples':
            CameraSimples()
        if escolha =='Angulo Corporal':
            ModeloCorpo()
    #gerencia comandos do usuario
    if eventos=='Iniciar Exame' :#AND valores['ImgSel']=='Camera Simples'
        CamIndex= int(valores['SelCamera'])
        HabilitarCamera = True
        cap = cv2.VideoCapture(CamIndex)
    if eventos == 'Interromper':
        HabilitarCamera=False
    if eventos == sg.WINDOW_CLOSED:
        break# a ultima comparação de evento é para fechar a janela