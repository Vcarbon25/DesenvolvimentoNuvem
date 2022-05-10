from PySimpleGUI import PySimpleGUI as sg
import cv2

sg.theme('SandyBeach')

def Listar_cameras():
    index=0
    lista = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            lista.append(index)
        cap.release()
        index+=1
    return lista
       
def CameraSimples():
    global CamIndex
    cap = cv2.VideoCapture(CamIndex)
    global HabilitarCamera
    while HabilitarCamera:
        sucess, img = cap.read()
        ImgTamanho = cv2.resize(img, Tamanho_Imagem) #faz a imagem do tamanho do configurado pela tupla
        ImgTela = cv2.imencode(".png",ImgTamanho)[1].tobytes()
        principal["camera"].update(data=ImgTela)
    cap.release()


HabilitarCamera=True
camera_Width=320
camera_heigth = 240
Tamanho_Imagem=(camera_Width,camera_heigth)
cameras = Listar_cameras()

Exames=['Camera Simples','Angulo Corporal']
coluna_esquerda = [[sg.Image(filename="",key="camera")],[sg.Output(20,4)]]
SelCamera=int()
ImgSel=str()
coluna_do_meio = [[],[sg.Text('Camera: '),sg.OptionMenu(cameras,default_value='cam',key=SelCamera)],
[sg.Text('Selecione O Exame :'), sg.OptionMenu(Exames,default_value='escolha',key=ImgSel)],
[sg.Button('Iniciar Exame'),sg.Button('Interromper')]]

layout =[coluna_esquerda,coluna_do_meio]
principal = sg.Window('V5 do TCC',layout).finalize()

while True:
    eventos, valores = principal.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos=='Iniciar Exame' :#AND valores['ImgSel']=='Camera Simples'
        CamIndex= valores['cam']
        HabilitarCamera = True
        cap = cv2.VideoCapture(CamIndex)
        