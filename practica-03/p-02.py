# Dado un texto generar una estructura que permita acceder directamente a una lista de palabras
# según la cantidad de caracteres de cada una. Es decir que cada palabra esté asociada al número
# de caracteres que tiene. Nota: las palabras no tienen que estar repetidas, y se debe tener en
# cuenta mayúsculas y minúsculas, espacios, comas y puntos.

frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás 
que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear 
realizar una búsqueda y reemplazo en un gran número DE archivos de 
texto,o renombrar y reorganizar un montón de archivos con fotos de una 
manera compleja. Tal vez quieras escribir alguna pequeña base de datos 
personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'''



dic_palabras = {}
palabras = frase.rsplit("\n")
frases = "".join(frases for frases in palabras)
lista_palabras = frases.rsplit(' ')
non_repeat = set(lista_palabras)
conteo = []

for item in non_repeat:
    conteo.append((len(item),item))

conteo.sort( key = lambda x: x[0] )
aux = []

index = 0
for item in conteo:
    if index == 0:
        index = item[0]
        aux.append(item)
    elif index == item[0]:
        aux.append(item[1])
    elif index != item[0]:
        dic_palabras[index] = aux[::]
        aux.clear()
        index = item[0]
        aux.append(item[1])

print(dic_palabras)