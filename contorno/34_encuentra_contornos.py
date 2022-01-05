import cv2
imagen=cv2.imread('D:/Repos/python/python-de-cero-hasta-reconocimiento-facial/PythonNoMatematicos/PythonNoMatematicos/contorno/contorno.jpg')

grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY )
tipoUmbral,umbral = cv2.threshold(grises, 100,255,cv2.THRESH_BINARY)
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


#Mostrar imagen
cv2.drawContours(imagen,contorno,-1,(251,63,52),3)
cv2.imshow('original',imagen)
print(jerarquia)
#cv2.imshow('grises',grises)
print(tipoUmbral)
#cv2.imshow('umbral',umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()
