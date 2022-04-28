import cv2
#usos básicos de câmera com e sem janela própria
'''cap = cv2.VideoCapture(0) #argumento é o indice da camera utilizada
while cap.isOpened(): #Fica em Loop enquanto a janela aberta
    sucess, img = cap.read()

    cv2.imshow('Camera',img)
    if cv2.waitKey(10)&0xFF == 27:  #fecha Com ESC
            break
cap.release()     #fecha a imagem da camera
cv2.destroyAllWindows()     #fecha a janela de display
'''#mostrar uma janela apenas com a imagem da câmera
#mostrar câmera em janela do tkinter
import tkinter as TK
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win = TK.Tk()

# Set the size of the window
win.geometry("700x500")

# Create a Label to capture the Video frames
label =TK.Label(win)
label.grid(row=0, column=0)
botao = TK.Button(win,text='but1')
botao2=TK.Button(win,text='But2')
botao.grid(row=0,column=1)
botao2.grid(row=1,column=0)
cap= cv2.VideoCapture(0)
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()
win.mainloop()
#essa acima é umajanela simples mostrando apenas um label com a imagem