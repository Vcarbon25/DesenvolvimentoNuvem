import cv2

class CamerasTCC:
    global HabilitarCameras
    HabilitarCameras=False
    def __init__(self):
       pass
    def Listar_cameras():
        index = 0
        arr = []
        while HabilitarCameras:
            cap = cv2.VideoCapture(index)
            if not cap.read()[index]:
                break
            else:
              arr.append(index)
            cap.release()
            index += 1
        return arr
    
