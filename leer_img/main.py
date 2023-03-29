import cv2

#leer la imagen a color
img = cv2.imread("..\\banco_img\\cat.jpg", cv2.IMREAD_COLOR)
h,w,c = img.shape
print(f"Image 1: Height: {h}, Width: {w}, Channels: {c}")
cv2.imshow('Imagen 1: ', img)
cv2.waitKey(0)

#leer la imagen en escala de grises
img = cv2.imread("..\\banco_img\\cat.jpg", cv2.IMREAD_GRAYSCALE)
h,w = img.shape
print(f"Image 2: Height: {h}, Width: {w}, Channels: 1")
cv2.imshow('Imagen 2: ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()