import tkinter as TK
from PIL import Image, ImageTk
import cv2

from ParteGráficaDoTCC import Bcadastro, ListaCameras

# Create an instance of TKinter Window or frame
raiz = TK.Tk()
#configura menu superior
top=raiz.winfo_toplevel()
raiz.BarraMenu = TK.Menu(top)
top['menu']=raiz.BarraMenu
BCadastro = TK.Button(top,text='Cadastrar Paciente')
BCadastro.grid(row=0,column=0)
BInfo = TK.Button(top,text='Informações do programa')
BInfo.grid(row=0,column=1)
# Set the size of the window
raiz.geometry("900x600")
#Criar funções auxiliares
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

# Create window to capture the Video frames
ECamera =TK.Label(raiz)
ECamera.grid(row=1, column=0)
cameraselect=TK.StringVar
ListaCameras=EncontrarCameras()
CameraSelect = TK.OptionMenu(raiz, cameraselect,*ListaCameras)
CameraSelect.grid(row=1,column=2)

BStart = TK.Button(raiz,text='Iniciar Exame')
botao2=TK.Button(raiz,text='But2')
BStart.grid(row=1,column=1)
botao2.grid(row=2,column=0)
cap= cv2.VideoCapture(0)
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   ECamera.imgtk = imgtk
   ECamera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   ECamera.after(20, show_frames)

show_frames()
raiz.mainloop()