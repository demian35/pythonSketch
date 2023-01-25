import cv2


imagen= cv2.imread("inserte su imagen (el nombre del archivo)")
#le pasamos la imagen con la que trabajaremos

#aplicamos filtro a la foto , en ese caso usamos la funcion cvtcolor y le pasamos el color gris de cv2
filtrogrises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#invertimos el flitro de grises
invert=cv2.bitwise_not(filtrogrises)

#aplicamos el fitro blur al invert
blurfilter=cv2.GaussianBlur(invert,(21,21),0)

#invertimos a blur
invertblur=cv2.bitwise_not(blurfilter)

#aplicamos el pencil sketch
pencilsketch=cv2.divide(filtrogrises,invertblur,scale=256.0)

#regresamos la imagen pintada a lapiz
cv2.imwrite("output.png",pencilsketch)