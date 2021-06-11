import math
CONSt= 17.31

d1 =  float( input("ingrese la distancia_1 (en metros)\n"))
d2 = float(input("ingrese la distancia_2 (en metros)\n"))
f = float(input("ingrese la frecuencia en Mhz \n"))

R = 17.31 * math.sqrt(  ((d1*d2)/(f*(d1+d2)))  )

print("===="*30 )
print("el radio de fresnel es : {:.2f} mts".format(R) )
print("===="*30 )

enter = input("presion enter para finalizar \n")