
# Utilizar como estructura de datos de referencia la generada en el ejercicio 3 y generar funciones
# que ejecuten lo siguiente:
# (a) Imprimir los 10 primeros puntajes de la estructura.
# (b) Imprimir los datos de los usuarios ordenados alfabéticamente por apellido.
# (c) Imprimir los datos de los usuarios ordenados por nivel alcanzado.
# Nota: utilice expresiones lambda para resolver los incisos.


jugadores = {
    'jose': [11, 1024, 23], 
    'emanuel': [4, 2324, 30], 
    'jefferson': [8, 8024, 90], 
    'ricardo': [1, 56524, 10], 
    'miguel': [3, 24, 5], 
    'esteban': [3, 5240, 580], 
    'carlos': [4, 3440, 60], 
    'rodrigo': [6, 240, 40], 
    'nacho': [7, 120, 230], 
    'ivan': [12, 540, 110], 
    'ramiro': [45, 45640, 140]}

diezPrimeros = lambda x:x[1][1]
porApellido = lambda x:x[0]
porNivel = lambda x:x[1][0]

print ("los diez primeros son --> {}".format( sorted(jugadores.items(),key=diezPrimeros,reverse=True)[0:10] ))
print ("\nordenados por nombre --> {}".format( sorted(jugadores.items(),key=porApellido)))
print ("\nordenados por nivel --> {}".format( sorted(jugadores.items(),key=porNivel)))