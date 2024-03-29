import cv2
import os
import tkinter as tk
from tkinter import filedialog #examinar ordenador


##funcion para cargar la imagen
def cargaImagen():
    rutaimagen=filedialog.askopenfile()
    if rutaimagen:
        imagen=cv2.imread(rutaimagen.name)
        return imagen,os.path.dirname(rutaimagen.name)
    else:
        return None


def aplicaFiltro(opcion,label_resultado):
    imagen, directorio=cargaImagen()
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
        nombre_archivo = None
        if opcion==1:
            nombre_archivo = "outputgrey.jpg"
            cv2.imwrite(os.path.join(directorio, nombre_archivo), filtrogrises)
        elif opcion==2:
            nombre_archivo = "outputblur.jpg"
            cv2.imwrite(os.path.join(directorio, nombre_archivo), blurfilter)
        elif opcion==3:
            nombre_archivo = "outputpencilsketch.jpg"
            cv2.imwrite(os.path.join(directorio, nombre_archivo), pencilsketch)
        else:
            print("Opcion no valida")
        if nombre_archivo:
            print(f"Imagen guardada en: {os.path.join(directorio, nombre_archivo)}")
            mensaje = f"Imagen guardada en: {os.path.join(directorio, nombre_archivo)}"
            label_resultado.config(text=mensaje)
            
#metodo main para crear la interfaz grafica del programa
def main():
    root=tk.Tk()
    root.title("Fitros") #titulo para la interfaz
    root.geometry("800x600")  # Establece el tamaño de la ventana
    
    #botones para aplicar los filros
    botongrises=tk.Button(root, text="efecto de grises", command=lambda:aplicaFiltro(1))
    botongrises.pack(pady=5)
    
    botonblur=tk.Button(root,text="efecto blur", command=lambda:aplicaFiltro(2))
    botonblur.pack(pady=5)
    
    botonsketch=tk.Button(root, text="efecto lapiz",command=lambda:aplicaFiltro(3))
    botonsketch.pack(pady=5)
    
    ## Etiqueta para mostrar el resultado
    label_resultado = tk.Label(root, text="")
    label_resultado.pack()
    
    root.mainloop()
    
if __name__=="__main__":
     main()
            