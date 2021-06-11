# Generar un menú que te permita ingresar dos números por teclado y luego realizar una de las
# siguientes operaciones:

# suma: +
# resta: -
# multiplicación: *
# división: /

# Se debe mostrar el resultado de la operación

num1=0
num2=0

def ingresarNumeros():
    global num1,num2
    print("ingrese el primer numero\n")
    num1=int(input())
    print("ingrese el segundo numero\n")
    num2=int(input())

def panelOpciones():
    print(""" ingrese alguno de los siguientes simbolos para realizar una operación
        suma: +
        resta: -
        multiplicación: *
        división: /
""")


ingresarNumeros()
panelOpciones()
operacion = input()
if operacion == '+':
    print("la suma es:  {0} + {1} = {2}".format(num1,num2,num1+num2))
elif operacion == '-':
    print("la resta es:  {0} - {1} = {2}".format(num1,num2,num1-num2))
elif operacion == '*':
    print("la multiplicacion es:  {0} * {1} = {2}".format(num1,num2,num1*num2))
elif operacion == '/':
    print("la division es:  {0} / {1} = {2}".format(num1,num2,num1/num2))
else:
    print("comando no valido")

print("="*30+'\n')