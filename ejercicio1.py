#ejercicio 1
tupla = ("pala","pelota","red","pared")
print(tupla)
lista = list(tupla)
#convierto la tupla en lista 

lista.append("tubo")
print(lista)
#la lista si se puede modificar y la tupla no

print(lista [1])

print(len(lista))

print('pala' in lista)
print('toalla' in lista)

lista[1:2]=["carro"]
print(lista)

lista.clear()
print (lista)