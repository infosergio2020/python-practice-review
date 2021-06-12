# Escribir una función que reciba al menos un argumento y opcionalmente una lista de argumentos
# variables y una lista de argumentos con nombre. El argumento fijo deberá ser la operación que
# se desea hacer con lista de números que se reciba como variable y los argumentos con nombre
# corresponden a los datos de la persona que solicitó la operación. Las operaciones posibles son:
# “+” y “*”. Los datos con nombre variables pueden ser: nombre, apellido y dirección.
# Nota: investigar la función reduce del módulo functools

op_validas = {'+','-','*','/'}

def sumador(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Suma: ",sum)

def imprimir(**dato):
    print("\nTipo de datos de argumento:",type(dato))
    for key, value in dato.items():
        print("{} es {}".format(key,value))


def hibrido (op='+',*num,**data):
    if op not in op_validas:
        print("la operacion que seleccionó no es valida :C ")
    else:
        print("Datos de la persona que va a realizar la operación\n")
        for key, value in data.items():
            print("{} es {}".format(key,value))
        if num and len(num) >= 2:
            result = 0
            if op == '+':
                for n in num:
                    result+= n
                print("resultado: ",result)
            elif op == '-':
                for n in num:
                    result-= n
                print("resultado: ",result)
            elif op == '*':
                result = 1
                for n in num:
                    result*= n
                print("resultado: ",result)
            else:
                result = 1
                for n in num:
                    result/= n
                print("resultado: ",result)
        else:
            print("deben haber almenos 2 numeros para realizar la operación")

hibrido('+', 2,3,4,5,12,23,43,14, nombre='sergio',telefono='4323525',ciudad='La Plata', email='asdf@gmail.com')