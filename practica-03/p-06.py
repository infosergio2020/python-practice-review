# Usando el diccionario del Ejercicio 5, acceder a las coordenadas (x,y) y, según el color asociado,
# ejecutar una función asociada a la misma. Las funciones pueden plantear la resolución de
# ejercicios simples como ser:
# (a) Suma de dos números que se generen en forma aleatoria cada vez que se llama a la función,
# reciba el resultado por teclado y verifique el resultado.
# (b) Dada la estructura que contiene palabras clasificadas según su acentuación:
# palabras = [('grave',['molesto']), ('aguda',['ratón']),
# ('esdrujula',['murciélago'])]
# Cada vez que se ejecuta la función se elige una palabra en forma aleatoria, se consulta
# al usuario sobre el tipo de palabra que cree que es por su acentuación y se verifica la
# respuesta.

import random
# PARTE A
# def suma (x=random.randint(0,9),y=random.randint(0,9)): 
#     return x+y
# def resta (x=random.randint(0,9),y=random.randint(0,9)):
#     return x-y
# def multiplicacion ( x=random.randint(0,9),y=random.randint(0,9)): 
#     return x*y
# def division (x=random.randint(0,9),y=random.randint(0,9)): 
#     return x/y

# dic = {
#         'blanco': [(2, 3),suma()], 
#         'negro': [(8, 8),resta()], 
#         'amarillo': [(-5, -8),multiplicacion()], 
#         'rojo': [(5, 6),division()], 
#         'azul': [(10, 2),suma()]
#         }

# print("ingrese un color \n")
# color = input()
# print ("color {} coordenada {} funcion {}".format(color,dic[color][0],dic[color][1]))

# PARTE B

palabras = [
            ('grave',['molesto']), 
            ('aguda',['ratón']), 
            ('esdrujula',['murciélago'])
            ]

# comienzo de la declaracion de funciones
def preguntar(pal):
    pregunta = random.choice(pal)
    print("¿Qué tipo de palabra es: {} según su tipo de ascentuacion?".format(pregunta[1][0]))
    print("¿ grave, aguda o esdrujula ?")
    respuesta = input()
    evaluar(pregunta,respuesta)

def evaluar(preg,res):
    if preg[0] == res:
        print("Correcto!!!")
    else:
        print("No!!! , la palabra es {}".format(preg[0]))
# Fin de la declaracion de funciones

preguntar(palabras)
