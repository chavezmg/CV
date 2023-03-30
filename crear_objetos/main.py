import cv2


img = cv2.imread("../banco_img/messi.jpg")
resized_img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#dimensiones imagen
h, w, c = resized_img.shape

#dibujamos una linea
resized_img = cv2.line(resized_img, pt1=(0,0), pt2=(int(w/2), int(h/2)), 
                       color=(255,0,0), thickness=5)

#dibujamos un rectangulo
resized_img = cv2.rectangle(resized_img, pt1=(int(w/2)-100, int(h/2)-100),
                             pt2=(int(w/2)+100, int(h/2)+100), color=(0,255,0))

#dibujamos un circulo
resized_img = cv2.circle(resized_img, center=(int(w/2), int(h/2)), 
                         radius=100, color=(0,0,255))

#dibujamos un circulo relleno
resized_img = cv2.circle(resized_img, center=(int(w/2)-200, int(h/2)), 
                         radius=30, color=(0,0,255), thickness=cv2.FILLED)

#escribimos un texto
resized_img = cv2.putText(resized_img, text="Messi campeon", org=(50,50), 
                          fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,50,255), thickness=2)

cv2.imshow("Imagen: ", resized_img)

cv2.waitKey(0)