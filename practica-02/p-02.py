# Dada una lista como la utilizada en el ejercicio 1 genere una lista nueva que contenga solamente
# las coordenadas y ordénelas. Investigue la función sort. Ejemplo: si la lista original es:

# tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']
# La lista generada sería:
# [(4, 14), (6, 34), (33, 15), (410, 134)]

def generarListaTuplas(lista):
    aux = []
    for item in lista:
        x,separator,y= item.split(' ')[1].partition(',')
        tupla = (int(x),int(y))
        aux.append(tupla)
    return aux

tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']
 
resultado = generarListaTuplas(tam)
resultado.sort(key=lambda k:k[0])
print('='*30+'\n')
print(resultado)
print('='*30)