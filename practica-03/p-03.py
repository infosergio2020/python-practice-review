jugadores = [
            ('jose',11,1024,23),
            ('emanuel',4,2324,30),
            ('jefferson',8,8024,90),
            ('ricardo',1,56524,10),
            ('miguel',3,24,5),
            ('esteban',3,5240,580),
            ('carlos',4,3440,60),
            ('rodrigo',6,240,40),
            ('nacho',7,120,230),
            ('ivan',12,540,110),
            ('ramiro',45,45640,140)
            ]


# LECTURA DE DATOS POR STANDAR SYSTEM INPUT
# def reg_data_user():
#     nombre = input("introduzca nombre \n")
#     nivel = input("introduzca nivel \n")
#     puntaje = input("introduzca puntaje \n")
#     tiempo = input("introduzca tiempo \n")
#     return  nombre,nivel,puntaje,tiempo

# nombre,nivel,puntaje,tiempo = reg_data_user()

# LECTURA DE MOCK DE DATOS

# Para registrar las actividades de un usuario en un juego dado se requiere guardar los siguientes
# datos: nombre del jugador, nivel alcanzado en el juego, puntaje máximo y tiempo de juego.
# Realizar los siguientes items con esta estructura:
# Seleccione la estructura que considere más adecuada para almacenar la información de
# varios usuarios ingresados desde teclado. Tener en cuenta que se necesita acceder a un
# usuario determinado en forma directa sin recorrerla.
# Con la estructura generada, imprimir los datos de un usuario dado sin recorrer la estructura.
# ¿La elección sobre la estructura fue adecuada? ¿Cuál usó?

def maxpuntaje(dic):
    # return max(dic,key=dic.get)
    return max(dic,key= lambda k:dic[k][1])

def guardar(datos,dic):
    if datos[0] in dic:
        if dic[datos[0]][1] < datos[1]:
            dic[datos[0]] = datos[1]

def ordenar(dic,rev):
    return sorted(dic.items(),key=lambda x: x[1][1] ,reverse=rev)
    

dic_jugadores = {}

for jugador in jugadores:
    dic_jugadores[jugador[0]] = [jugador[1],jugador[2],jugador[3]]

print("jugadores: \n")
print("--> {0}".format( list(dic_jugadores.keys()) ))

nomb = input("\n introduzca un nombre de jugador para ver mas información \n")
print(dic_jugadores[nomb])

print("\n el mayor puntaje lo tiene --> {0} \n".format(maxpuntaje(dic_jugadores)))

print("\n puntuacion en orden \n")
print(ordenar(dic_jugadores,False))


print(dic_jugadores)