import math

print("\n \n Nyquist C = 2 B log2 ( M ) opcion 1\n")
print("Nyquist B = C / ( 2 * log2(M) ) opcion 2\n")
print("""siendo M el n° de señales discretas o niveles de voltage
ej:

1bit -->(0 o 1) = 2^1 (M=2 niveles)
1bit -->(00 o 11) = 2^2 (M=4 niveles)
1bit -->(000 o 111) = 2^3 (M=8 niveles)
""")



opc =  int( input("seleccione 1 o 2 segun la formula que desea probar\n"))

if(opc == 1):
    b =  float( input("ingrese el ancho de banda --> B (medido en Hz)\n"))
    m = float(input("ingrese el nivel --> M  (sin unidad)\n"))
    c = ((2*b) * math.log2(m))
    print("===="*30 )
    print(" C = 2 B log2 ( M ) --> C = : {:.2f} bps".format(c) )
    print("===="*30 )
else:
    c =  float( input("ingrese el velocidad de transmision --> C (medido en bps)\n"))
    m = float(input("ingrese el nivel --> M  (sin unidad)\n"))
    b = (c/(2*math.log2(m)))
    print("===="*30 )
    print(" B = C / ( 2 * log2(M) ) por lo que el resultado es --> B = : {:.2f} bps".format(b) )
    print("===="*30 )


enter = input("presion enter para finalizar \n")