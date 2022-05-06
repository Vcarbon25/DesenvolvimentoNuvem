import tkinter as TK
import cv2
from PIL import Image, ImageTk

from ParteGraficaTCCV2 import ListaCameras

raiz = TK.Tk()

# Set the size of the window
raiz.geometry("1040x500")
raiz.title('Parte Grafica TCC V4')
cap= cv2.VideoCapture(0)
def CameraSimples():
    sucess, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    show_frames(img)
def show_frames(cv2image):
   # Get the latest frame and convert into Image
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   LCamera.imgtk = imgtk
   LCamera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   LCamera.after(20, CameraSimples)

def Encontrar_Cameras():
    ListaCameras=[]
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
LCamera =TK.Label(raiz)
LCamera.grid(row=0, column=0,rowspan=6)
botao = TK.Button(raiz,text='but1',padx=30)
botao.grid(row=0,column=1)



CameraSimples()
raiz.mainloop()