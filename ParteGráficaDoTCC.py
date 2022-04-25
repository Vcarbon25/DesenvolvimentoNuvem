#protótipo de tela com exibição da câmera simples
import tkinter as TK
import cv2
from PIL import Image, ImageTk

def EncontrarCameras():
    ListaCameras =[]
    index=0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            ListaCameras.append(index)
        cap.release()
        index+=1
    return ListaCameras

global HabilitarCamera
HabilitarCamera=0
def ShowCamera():
    IndiceCamera = int(cameraselect)
    if HabilitarCamera == 1:
        pass
        


raiz = TK.Tk()
raiz.geometry("600x600")
#preparar o menu de cima
top = raiz.winfo_toplevel()
raiz.BarraMenu = TK.Menu(top)
top['menu'] = raiz.BarraMenu
Bcadastro = TK.Button(top, text="  Cadastrar Paciente  ",border=1)
Bcadastro.grid(row=0,column=0)
Bsaida = TK.Button(top,text="  Definir saida  ")
Bsaida.grid(row=0,column=1)
Binfo = TK.Button(top, text='  Sobre  ')
Binfo.grid(row=0,column=2)
#SeriaCamera = ImageTk.PhotoImage(Image.open('EsquemaLandmarksHolistico'))
ECamera = TK.Label(raiz,text='Camera vai aqui', borderwidth=3)
ECamera.grid(row=1,column=1,columnspan=2,rowspan=3)
EQEsq=TK.Label(raiz, text="Angulo Q esquerdo")
EQEsq.grid(row=2,column=0)
EQDir = TK.Label(raiz,text='Angulo Q direito')
EQDir.grid(row=2,column=1)
global cameraselect
cameraselect = TK.StringVar()
ListaCameras = EncontrarCameras()

CameraSelect=TK.OptionMenu(raiz, cameraselect, *ListaCameras)
CameraSelect.grid(row=1,column=3)
BStart = TK.Button(raiz,text='Iniciar Exame')
BStart.grid(row=2,column=3)
raiz.mainloop()