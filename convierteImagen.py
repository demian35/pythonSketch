import cv2
import tkinter as tk
from tkinter import filedialog #examinar ordenador


##funcion para cargar la imagen
def cargaImagen():
    rutaimagen=filedialog.askopenfile()
    if rutaimagen:
        imagen=cv2.imread(rutaimagen)
        return imagen
    else:
        return None


def aplicaFiltro(opcion):
    imagen=cargaImagen()
    if imagen is not None:
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
        if opcion==1:
            cv2.imwrite("outputgrey.jpg", filtrogrises)
        elif opcion==2:
            cv2.imwrite("outputblur.jpg",blurfilter)
        elif opcion==3:
            cv2.imwrite("outputpencilsketch.jpg",pencilsketch)
        else:
            print("Opcion no valida")
            