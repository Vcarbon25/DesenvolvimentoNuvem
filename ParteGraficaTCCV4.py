import tkinter as TK
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import time
raiz = TK.Tk()

# Configurações Básicas da Janela
raiz.geometry("1040x500")
raiz.title('Parte Grafica TCC V4')
cap= cv2.VideoCapture(0)
#definição de funções auxiliares
def CameraSimples():
    sucess, img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    show_frames(img)

#habilitar exibição de fps
ptime =0
ctime=0
def show_frames(cv2image):
   #colocar a contagem de fps na imagem do opencv
   global ctime
   ctime=time.time()
   global ptime
   fps=1/(ctime-ptime)
   ptime = ctime
   nfps=int(fps) #converte o n real para n inteiro
   txtfps=str(nfps)
   cv2.putText(cv2image,txtfps,(10,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,50),3)
   # converter imagem para ser usada no tkinter
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   LCamera.imgtk = imgtk
   LCamera.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   LCamera.after(20, Modelo_Corpo)

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



def Modelo_Corpo():
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
        sucess, frame=cap.read()
        imagemRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = holistic.process(imagemRGB)
        imagemBGR = cv2.cvtColor(imagemRGB,cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(imagemBGR,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(100,255,100),thickness=4,circle_radius=6),
        mp_drawing.DrawingSpec(color=(100,100,255),thickness=3,circle_radius=5))
        show_frames(imagemBGR)

#COnfigura a Parte gráfica da janela

LCamera =TK.Label(raiz)
LCamera.grid(row=0, column=0,rowspan=6)
botao = TK.Button(raiz,text='but1',padx=30)
botao.grid(row=0,column=1)

Modelo_Corpo()
raiz.mainloop()