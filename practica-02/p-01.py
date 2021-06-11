# Dada una lista de strings con el siguiente formato:
# tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']

# Donde im1, im2, etc son los nombres de las imágenes y la parte de números representa el valor
# de una coordenada (x, y). Se solicita que arme dos listas que contengan, nombre y luego una
# tupla de las coordenadas en formato de números. Una de las listas debe contener los datos en
# las cuales el valor de x es mayor o igual a un número ingresado por teclado y la otra, contendrá
# los datos de las imágenes cuyo valor de coordenada sea menor al número ingresado. Tener en
# cuenta que los datos de la lista original son strings y que los números de la lista generada deben
# ser enteros. Se espera que se muestre el siguiente resultado, si el dato ingresado por el teclado
# fuera 30:

# lista1 = ['im2', (33, 15), 'im4', (410, 134)]
# lista2 = ['im1', (4, 14), 'im3', (6, 34)]
# Nota: puede utilizar la función string.partition que permite separar un string y asignar a
# variables. Investigue su utilización.


# def crearLista():
#     iter = int(input("ingrese la cantidad de imagenes a insertar\n"))
#     lista = []
#     for item in range(iter):
#         name = input("ingrese nombre de image\n")
#         coord = input("coordernada ej: 32,45\n")
#         lista.append(name+' '+coord)
#     return lista

# def imprimirResultado(aux = []):
#     print("="*30)
#     print(aux)
#     print("="*30)


# lista = crearLista()
# imprimirResultado(lista)

tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

numb = int(input("ingrese un numero\n"))
menor = []
mayor = []

for item in tam:
    img,coord=item.split(' ')
    x,separator,y = coord.partition(',')
    tupla = (int(x),int(y))
    if(int(x) > numb):
        mayor.append(img)
        mayor.append(tupla)
    else:
        menor.append(img)
        menor.append(tupla)

print("a continuación se vana a imprimir las listas \n")
print("="*30)
print('lista 1 = {}'.format(mayor))
print('lista 2 = {}'.format(menor))
print("="*30+'\n')