# Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas
# y minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.


frase = """Si trabajás mucho CON computadoras, eventualmente encontrarás que te
gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una
búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y
reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación especializada
con interfaz gráfica, o UN juego simple."""

# convierto las palabras en minusculas y luego las separo por espacio en una lista eliminando los saltos de linea
lista_palabras = frase.lower().rsplit()

#convierto la lista de palabras en un conjunto para eliminar las palabras repetidas y agarro el conjunto y los transformo a lista
print(list(set(lista_palabras))) 