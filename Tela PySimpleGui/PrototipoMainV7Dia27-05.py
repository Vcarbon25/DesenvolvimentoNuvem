import PySimpleGUI as sg
import cv2

sg.theme=('SandyBeach')

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
janela=sg.Window('V7DoTCC',layout).finalize()
HabilitarCamera=False
escolha='null'
while True:
    eventos, valores = janela.read()
    CamIndex=int(valores['CamSel'])
    cap = cv2.VideoCapture(CamIndex)
    
    if eventos == 'Iniciar Exame':
        HabilitarCamera = True
        escolha = valores['ImgSel']
    if eventos == 'Interromper':
        HabilitarCamera=False
        escolha='null'
    
    if eventos==sg.WINDOW_CLOSED:
        break
        