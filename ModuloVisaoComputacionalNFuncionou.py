import cv2
from cv2 import cvtColor
import mediapipe as MP

class ModelosCorporais:
    def __init__(self):
        global mpHands
        mpHands = MP.solutions.hands
        global hands
        hands = mpHands.Hands()  #essas duas linhass anteriores preparam o modelo de mãos, para possivel uso
        mp_holistic = MP.solutions.holistic
        holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5)
        global mp_draw
        mp_draw = MP.solutions.drawing_utils

    def ModeloMaos(frame):
        imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        maosResults = hands.process(imgRGB)
        for handLms in maosResults.multi_hand_landmarks:
            pass
        mp_draw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)

#o principal serve para testar os módulos da classe

cap = cv2.VideoCapture(0)
Teste = ModelosCorporais()
while True:
    frame, sucess = cap.read()
    frame = Teste.ModeloMaos(frame)
    cv2.imshow(frame)
    if cv2.waitKey(10)&0xFF ==27:
        break