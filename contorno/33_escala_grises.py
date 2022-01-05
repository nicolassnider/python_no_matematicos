import cv2
imagen=cv2.imread('D:/Repos/python/python-de-cero-hasta-reconocimiento-facial/PythonNoMatematicos/PythonNoMatematicos/contorno/contorno.jpg')

grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY )
umbral = cv2.threshold(grises, 100,255,cv2.THRESH_BINARY)


#Mostrar imagen
cv2.imshow('original',imagen)
cv2.imshow('grises',grises)
cv2.waitKey(0)
cv2.destroyAllWindows()
