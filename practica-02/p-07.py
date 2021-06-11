# Dado un string ingresado por teclado, determinar si es un palíndromo. Investigue la operación
# sobre strings que permite invertirlos. Tener en cuenta que puede haber mayúsculas y minúsuclas
# mezcladas en el string ingresado.

palabra = input("ingrese una palabra \n").lower()

invertida= palabra[::-1]

print(invertida == palabra)