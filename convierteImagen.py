import cv2


filename= r"C:\Users\josed\OneDrive\Imágenes\IMG_3110.JPG"
#le pasamos la imagen con la que trabajaremos
imagen=cv2.imread(filename)

#aplicamos filtro a la foto , en ese caso usamos la funcion cvtcolor y le pasamos el color gris de cv2
filtrogrises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#invertimos el flitro de grises
invert=cv2.bitwise_not(filtrogrises)

#aplicamos el fitro blur al invert
blurfilter=cv2.GaussianBlur(invert,(21,21),0)

#invertimos a blur
invertblur=cv2.bitwise_not(blurfilter)