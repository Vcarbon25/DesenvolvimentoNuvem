from PySimpleGUI import PySimpleGUI as sg
import cv2
import Auxiliar3ponto5
sg.theme('SandyBeach')

camera_Width=320
camera_heigth = 240
Tamanho_Imagem=(camera_Width,camera_heigth)
Sistema_De_Cameras = Auxiliar3ponto5.Cameras_TCC
cameras = Sistema_De_Cameras.Listar_cameras()
Exames=['Camera Simples','Angulo Quadricipetal']
coluna_esquerda = [[sg.Image(filename="",key="camera")],[sg.Output(20,4)]]
coluna_do_meio = [[],[sg.Text('Camera: '),sg.OptionMenu(cameras,default_value='camera')],
[sg.Text('Selecione O Exame :'), sg.OptionMenu(Exames,default_value='escolha')],
[sg.Button('Iniciar Exame'),sg.Button('Interromper')]]

layout =[coluna_esquerda,coluna_do_meio]
principal = sg.Window('V3.5 do TCC',layout)

while True:
    pass