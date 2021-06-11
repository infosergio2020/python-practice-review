# Dado un string ingresado por teclado determinar si la cantidad total de veces que aparece cada
# letra es un número primo. Veamos un ejemplo:

cadena = input("ingrese una cadena\n")
ocurrencias = []
contador = []

for c in cadena:
    if c not in ocurrencias:
        if c != ' ':
            ocurrencias.append(c)
            contador.append((c,cadena.count(c)))

print('\n'*5+'='*30+'\n'+cadena+'\n'+'='*30)
for o in contador:
    if o[1] >1:
        print ("""La letra {0} aparece: {1} veces""".format(o[0],o[1]))
    else:
        print ("""La letra {0} aparece: {1} vez""".format(o[0],o[1]))
    
