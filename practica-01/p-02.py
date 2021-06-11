#  Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras
# (separadas por ’ ’), y sobre ella, informe la cantidad de palabras en las que se encuentra el
# string. No importan las mayúsculas y minúsculas


frase = input("ingrese una frase \n")
palabra = input("ingrese una palabra \n")

esIgual = lambda p: p == palabra 
result = list(filter(esIgual,frase.lower().split(' ')))
print(len(result))