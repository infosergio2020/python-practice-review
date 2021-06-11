# Dada una lista con varios strings, generar una nueva lista que contenga SOLO aquellos
# string que representen valores enteros. La misma debe quedar ordenada. Investigue la función
# string.isdecimal(). Ejemplo: si la lista original es:


lista_original = ['Auto', '123', 'Viaje', '50', '120']

lista_nueva = [ int(item) for item in lista_original if item.isdecimal()]
lista_nueva.sort(key=lambda k:k)

print(lista_nueva)