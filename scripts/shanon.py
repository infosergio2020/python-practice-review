import math


print("\n \n primera ley de Shannon C = B log 2 ( 1 + S/N ) \n \n")

b =  float( input("ingrese el ancho de banda --> B (medido en Hz)\n"))
sn = float(input("ingrese la señal ruido --> S/N  (en veces)\n"))
c = b * math.log2(1+sn)

print("===="*30 )
print("la primera ley de Shannon establece C = B log 2 ( 1 + S/N )  por lo que el resultado es --> C = : {:.2f} bps".format(c) )
print("===="*30 )

enter = input("presion enter para finalizar \n")