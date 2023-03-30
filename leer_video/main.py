import cv2

#leemos video
cap = cv2.VideoCapture("../banco_vid/video1.mp4")

while (True):
    succ, img = cap.read()     #succ: succesful, img: fotograma leido
    img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)    #redimensiono el video porque es muy grande
    if not succ:                #se acabó el video
        break
    cv2.imshow("video: ", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):   #tecla para salir, solo con esta tecla se sale
        break

cap.release()
cv2.destroyAllWindows()