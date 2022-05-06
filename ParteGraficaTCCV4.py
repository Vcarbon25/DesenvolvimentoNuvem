import tkinter as TK
import cv2
from PIL import Image, ImageTk
import mediapipe as mp

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
LCamera =TK.Label(raiz)
LCamera.grid(row=0, column=0,rowspan=6)
botao = TK.Button(raiz,text='but1',padx=30)
botao.grid(row=0,column=1)
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

CameraSimples()
raiz.mainloop()