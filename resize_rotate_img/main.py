import cv2

#leemos imagen
img = cv2.imread('..\\banco_img\\messi.jpg', cv2.IMREAD_COLOR)
resize_img = cv2.resize(img, (300,300))
resize_img2 = cv2.resize(img, (0,0), fx=0.2, fy=0.2)    #30% en 'X' y 30% en 'Y'

#mostramos imagen real
cv2.imshow("Messi 1: ", img)
cv2.waitKey(0)
#mostramos imagen alterada 1
cv2.imshow("Messi 2: ", resize_img)
cv2.waitKey(0)
#mostramos imagen alterada 2
cv2.imshow("Messi 3: ", resize_img2)
cv2.waitKey(0)

#cortamos un "area de interes"
cropped_img = img[50:500, 100:450]     #los pixeles de la imagen funcionan como lista
cv2.imshow("Messi 4: ", cropped_img)
cv2.waitKey(0)

#rotamos la imagen 90 grados en sentido horario y antihorario
cropped_img1 = cv2.rotate(cropped_img, cv2.ROTATE_90_CLOCKWISE)
cropped_img2 = cv2.rotate(cropped_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Messi 5: ", cropped_img1)
cv2.imshow("Messi 6: ", cropped_img2)
cv2.waitKey(0)