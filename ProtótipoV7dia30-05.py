import cv2, PySimpleGUI as sg

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


cap = cv2.VideoCapture(0)       # Setup the camera as a capture device

while True:                     # The PSG “Event Loop”

    event, values = janela.Read(timeout=20, timeout_key='timeout')      # get events for the window with 20ms max wait

    if event is None:  break                                            # if user closed window, quit

    janela.FindElement('camera').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes()) # Update image in window