# Generar un menú que te permita realizar las siguientes opciones:

# Menú de opciones para la lista de números a ingresar:
# 1: ingresar números
# 2: ordenar números
# 3: calcular el máximo
# 4: calcular el mínimo
# 5: calcular el promedio
# 0: para terminar

# Se debe repetir hasta que se ingrese la opción 0. Se debe permitir agregar números aún luego de
# haber utilizado las demás operaciones utilizando la opción 1. En caso que no se haya ingresado
# ningún número indicar que la lista está vacía. Investigue las funciones max, min y sum


numeros = []

def panelOpciones():
    print("""
Menú de opciones para la lista de números a ingresar:
1: ingresar números
2: ordenar números
3: calcular el máximo
4: calcular el mínimo
5: calcular el promedio
0: para terminar \n""")
    opcion = int(input())
    return opcion

# Funciones para manejos de lista BEGIN
def agregarNumero(lista = []):
    """inserta elementos en una lista si la lista esta vacia lo notifica"""
    if(len(lista)==0):
        print("la lista esta vacia \n")
    print("""ingrese numeros o ingrese 0 para finalizar""")
    num = int(input())
    while num != 0:
        lista.append(num)
        print("""ingrese numeros o ingrese 0 para finalizar""")
        num = int(input())
    print(lista)

def ordenarNumeros(lista):
    """retorna una lista de numeros ordenada en forma ascendente"""
    lista.sort()
    print(lista)

def calcularMinimo(lista):
    return min(lista)

def calcularMaximo(lista):
    return max(lista)

def calcularPromedio(lista):
    return (sum(lista)/len(lista))
# Funciones para manejos de lista END

def ejecutarOpciones(opcion):
    if(opcion == 1):
        agregarNumero(numeros)
    elif (opcion == 2):
        ordenarNumeros(numeros)
    elif (opcion == 3):
        print("el maximo es: {}".format(calcularMaximo(numeros)))
    elif (opcion == 4):
        print("el minimo es: {}".format(calcularMinimo(numeros)))
    elif (opcion == 5):
        print("el promedio es: {}".format(calcularPromedio(numeros)))
    elif (opcion == 0):
        print("saliendo de la aplicacion...")
    else:
        print("ingrese una opcion valida")

opc = panelOpciones()
while opc != 0:
    ejecutarOpciones(opc)
    opc = panelOpciones()