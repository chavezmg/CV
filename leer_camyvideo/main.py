import cv2
import numpy as np

#leemos video
cap0 = cv2.VideoCapture(0)   #este numero indica que camara, la default es 0
cap1 = cv2.VideoCapture("../banco_vid/video1.mp4") #"../banco_vid/video1.mp4"

while (True):
    succ0, img0 = cap0.read()     #succ: succesful, img: fotograma leido
    succ1, img1 = cap1.read()     #succ: succesful, img: fotograma leido
    
    if not succ1:                 #fin del video
        break

    img0_resized = cv2.resize(img0, (160, 120))    #redimensiono el video porque es muy grande
    img1_resized = cv2.resize(img1, (160, 120))    #redimensiono el video porque es muy grande
    
    fondo_negro = np.zeros((240,320, 3), np.uint8)      #altura, anchura, dimensiones(canales)

    h_img, w_img, c_img = fondo_negro.shape     #alto, ancho y canales del fondo negro
    
    fondo_negro[:h_img//2, :w_img//2] = img0_resized
    fondo_negro[:h_img//2, w_img//2:] = img1_resized
    fondo_negro[h_img//2:, w_img//2:] = img0_resized
    fondo_negro[h_img//2:, :w_img//2] = img1_resized

    cv2.imshow("cam 0 y 1: ", fondo_negro)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):   #tecla para salir, solo con esta tecla se sale
        break

cap0.release()
cap1.release()
cv2.destroyAllWindows()