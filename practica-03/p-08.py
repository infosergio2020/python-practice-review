# Definir dos funciones que reciban una cantidad variable de argumentos: a) una función que
# puede llegar a recibir hasta 30 números como parámetros y debe devuelva la suma total de
# los mismos; b) otra función que reciba un número variable de parámetros nombrados (usar
# **kwargs), e imprima dichos parámetros. De antemano no se sabe cuáles de los siguientes tres
# posibles parámetros se reciben:
# nombre
# apellido
# sexo

def sumador(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Suma: ",sum)

sumador(3,5)
sumador(4,5,6,7)
sumador(1,2,3,5,6)

def imprimir(**dato):
    print("\nTipo de datos de argumento:",type(dato))
    for key, value in dato.items():
        print("{} es {}".format(key,value))

imprimir(Nombre="Sita", Apellido="Sharma", Edad=22, Telefono=1234567890)
imprimir(Nombre="John", Apellido="Wood", Email="johnwood@gmail.com", Pais="Wakanda", Edad=25, Telefono=9876543210)