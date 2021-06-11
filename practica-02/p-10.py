# Dada una lista con nombres de imágenes:
# imagenes=['im1','im2','im3']
# Generar una estructura que asocie 3 coordenadas ingresadas por teclado (x1, y1) , (x2, y2) y
# (x3, y3) , con cada elemento de la lista (en el mismo orden en que son ingresadas). Además
# verifique, mientras se van ingresando las coordenadas, que no hayan repetidas para una misma
# imagen; en dicho caso deberá volver a ingresarla.


def nonRepeat(lista,coord):
    for item in lista:
        if item[1][0] == coord[0]:
            return False
        elif item[1][1] == coord[1]:
            return False
    return True

def insertItem(lista,imagen,coordenadas):
    if nonRepeat(lista,coordenadas):
        lista.append((imagen,coordenadas))
        return True
    else:
        return False



imagenes = ['im1','im2','im3']
mi_lista = []

coord_x = int(input("ingrese la coordenada x \n"))
coord_y = int(input("ingrese la coordenada y \n"))
i=0
while True:
    if i == len(imagenes):
        break
    if insertItem(mi_lista,imagenes[i], (coord_x,coord_y)): 
        print("se inserto correctamente\n")
        i+=1
    else:
        print("las coordenadas estan repetida ingrese coordenadas de nuevo\n")
    coord_x = int(input("ingrese la coordenada x \n"))
    coord_y = int(input("ingrese la coordenada y \n"))
    
print(mi_lista)