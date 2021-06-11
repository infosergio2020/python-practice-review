# Genere una nueva lista con todas las palabras de la frase dada en el ejercicio 1 en mayúsculas.


frase = """Si trabajás mucho con computadoras, eventualmente encontrarás que te
,!gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una
,!búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y
,!reorganizar un montón de archivos con fotos de una manera compleja. Tal vez
,!quieras escribir alguna pequeña base de datos personalizada, o una aplicación
,!especializada con interfaz gráfica, o un juego simple."""

lista_frase = frase.rsplit()
nueva_lista = []
for palabra in lista_frase:
    nueva_palabra = ''.join( p for p in palabra if p.isalnum() )
    nueva_lista.append(nueva_palabra.capitalize())

print(nueva_lista)