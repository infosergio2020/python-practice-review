# Escribir una función que reciba una cantidad variable de argumentos correspondientes a nombres
# de personas e imprima por pantalla los nombres enumerándolos.
# 0. Nombre 1
# 1. Nombre 2
# etc
# Nota: consultar el uso de enumerate.


def enumerador(*nombres):
    for count,value in enumerate(nombres):
        print("{0}. {1}".format(count,value))

enumerador('jose','pepe','carlos','esteban','maria','laura','viviana','ezequiel')