# Dada una lista con nombres de colores
# colores = ['azul','amarillo','rojo','blanco','negro']
# y una lista con coordenadas
# coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
# Generar una estructura que contenga coordenadas y un color asociado. La forma de asociar
# las coordenadas con el color debe ser aleatoria sin importar que se repitan los colores
# elegidos.
# Generar una estructura que contenga coordenadas y un color asociado. La forma de asociar
# las coordenadas con el color debe ser aleatoria sin que se repitan los colores.

import random

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dic={}
lista=[]

# for item in range(len(colores)):
#     coord = random.choice(coordenadas)
#     color = random.choice(colores)
#     lista.append((color,[coord]))

# for item in lista:
#     if item[0] in dic:
#         dic[item[0]].append(item[1][0])
#     else:
#         dic[item[0]] = item[1]

# print(dic)  

for item in range(len(colores)):
    coord = random.choice(coordenadas)
    color = random.choice(colores)
    coordenadas.remove(coord)
    colores.remove(color)
    dic[color] = coord
print(dic)    

# for color in colores:
#     rand_cood = random.choice(coordenadas)
#     dic[rand_cood] = color
# print(dic)
