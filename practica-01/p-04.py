# Dada la lista de palabras generada en el ejercicio 2, arme un string con la frase armada con
# todas ellas separadas por un único espacio en blanco.

frase = input("ingrese una frase \n")
# palabra = input("ingrese una palabra \n")

lista_frase = frase.rsplit()
nueva_lista = []
for palabra in lista_frase:
    nueva_palabra = ''.join( p for p in palabra if p.isalnum() )
    nueva_lista.append(nueva_palabra.capitalize())

print(' '.join( p for p in nueva_lista))