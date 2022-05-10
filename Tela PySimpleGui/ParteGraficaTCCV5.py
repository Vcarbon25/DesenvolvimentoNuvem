from PySimpleGUI import PySimpleGUI as sg
import cv2
import AuxiliarV5
sg.theme('SandyBeach')

camera_Width=320
camera_heigth = 240
Tamanho_Imagem=(camera_Width,camera_heigth)
Sistema_De_Cameras = AuxiliarV5.CamerasTCC
cameras = [0,1] #Sistema_De_Cameras.Listar_cameras()
Exames=['Camera Simples','Angulo Corporal']
coluna_esquerda = [[sg.Image(filename="",key="camera")],[sg.Output(20,4)]]
coluna_do_meio = [[],[sg.Text('Camera: '),sg.OptionMenu(cameras,default_value='camera')],
[sg.Text('Selecione O Exame :'), sg.OptionMenu(Exames,default_value='escolha')],
[sg.Button('Iniciar Exame'),sg.Button('Interromper')]]

layout =[coluna_esquerda,coluna_do_meio]
principal = sg.Window('V5 do TCC',layout).finalize()

while True:
    eventos, valores = principal.read()
    if eventos == sg.WINDOW_CLOSED:
        break