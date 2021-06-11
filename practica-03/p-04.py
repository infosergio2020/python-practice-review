# Dado el siguiente diccionario donde las claves son nombres de animales y los valores representan
# posiciones:
# anim={’Gato Montes’:2,’Yacare overo’:4,’Boa acuática’:5}
# Imprimir un string por cada animal de la estructura, reemplazando sus caracteres por el string
# ’_ ’ (inclusive los espacios en blanco) salvo el carácter correspondiente al valor del mismo.
# Ejemplo: Gato Montes tiene asociado el valor 2:

anim= {'Gato Montes':2,'Yacare overo':4,'Boa acuática':5}

for item in anim.items():
    lista=[]
    for c in range(len(item[0])):
        if c == item[1]:
            lista.append(item[0][item[1]])
        else:
            lista.append('_')
    print(''.join( c for c in lista))
    lista.clear()