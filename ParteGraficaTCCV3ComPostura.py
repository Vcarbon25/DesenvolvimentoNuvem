from logging import root
import tkinter as TK
from PIL import Image, ImageTk
import cv2
import time

from cv2 import FONT_HERSHEY_COMPLEX
raiz = TK.Tk()
#configura menu superior
top=raiz.winfo_toplevel()
raiz.BarraMenu = TK.Menu(top)
raiz.title('Se transforma no prog final')
top['menu']=raiz.BarraMenu
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

def Cadastrar_Paciente(): #Por enquanto só está mostrando mas sem fazer nada com essas informações
    JanelaCadastro = TK.Toplevel()
    JanelaCadastro.title('Cadastro de Paciente para exames')
    ENome = TK.Label(JanelaCadastro,text='Nome: ')
    InNome = TK.Entry(JanelaCadastro,width=70)
    ENome.grid(row=0,column=0)
    InNome.grid(row=0,column=1)
    EId=TK.Label(JanelaCadastro,text='Indentificação:')
    InId = TK.Entry(JanelaCadastro,width=50)
    EId.grid(row=1,column=0)
    InId.grid(row=1,column=1)
# Create window to capture the Video frames
ECamera =TK.Label(raiz)
ECamera.grid(row=1, column=0,rowspan=3)
cameraselect=TK.StringVar(raiz)
cameraselect.set("Seleção da câmera")
ListaCameras=EncontrarCameras()
opcao=[0,1,2,3,4]
CameraSelect = TK.OptionMenu(raiz,cameraselect, *ListaCameras)
CameraSelect.grid(row=1,column=1)
ListaExames=['camera simples','postura']#para cada função extra que colocar tem que botar o nome dela aqui também
Select_exam=TK.StringVar(raiz)
Select_exam.set('Escolher exame realizado')
ExamSelect=TK.OptionMenu(raiz,Select_exam,*ListaExames)
ExamSelect.grid(row=2,column=1)
BStart = TK.Button(raiz,text='Iniciar Exame')
BStart.grid(row=3,column=1)
cap= cv2.VideoCapture(0)
# Create an instance of TKinter Window or frame

BCadastro = TK.Button(top,text='Cadastrar Paciente',command=Cadastrar_Paciente())
BCadastro.grid(row=0,column=0)
BInfo = TK.Button(top,text='Informações do programa')
BInfo.grid(row=0,column=1)
# Set the size of the window
raiz.geometry("900x600")
#global ctime
ctime=0
global ptime
ptime =0
# Define function to show frame
def camera_simples():  
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   ctime = time.time()
   global ptime
   fps=1/(ctime-ptime)
   nfps = int(fps)
   txtfps=str(nfps)
   cv2.putText(cv2image, txtfps,(10,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(20,80,255))
   ptime=ctime #ele conseguiu fazer a contagem de fps aqui no tkinter tbm
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   ECamera.imgtk = imgtk
   ECamera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   ECamera.after(20, camera_simples)

camera_simples()
raiz.mainloop()