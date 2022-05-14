from PySimpleGUI import PySimpleGUI as sg
import cv2
import time

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

ptime=0
ctime=0
def ColocaNaTela(cv2img):
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
coluna_esquerda = [[sg.Image(filename="",key="camera")],[sg.Output(20,4)]]
SelCamera=int()
ImgSel=str()
coluna_do_meio = [[],[sg.Text('Camera: '),sg.OptionMenu(cameras,default_value='cam',key='SelCamera')],
[sg.Text('Selecione O Exame :'), sg.OptionMenu(Exames,default_value='escolha',key='ImgSel')],
[sg.Button('Iniciar Exame'),sg.Button('Interromper')]]

layout =[coluna_esquerda,coluna_do_meio]
principal = sg.Window('V5 do TCC',layout).finalize()

while True:
    eventos, valores = principal.read()
    
    if eventos=='Iniciar Exame' :#AND valores['ImgSel']=='Camera Simples'
        CamIndex= valores['SelCamera']
        HabilitarCamera = True
        cap = cv2.VideoCapture(CamIndex)
    if eventos == 'Interromper':
        HabilitarCamera=False
    if HabilitarCamera==True:
        escolha = valores['ImgSel']
        if escolha == 'Camera Simples':
            #CameraSimples()
            print('Seleção correta')
    if eventos == sg.WINDOW_CLOSED:
        break# a ultima comparação de evento é para fechar a janela