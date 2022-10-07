#ejercicio 2
  #set
set = set('pelota''pala''red')
print(set)

print(len(set))

print('z' in set)
print('p' in set)

set.add('c')
print(set)

set.clear()
print(set)

  #diccionario
diccionario = {"pala":"babolat", "pelota":"amarilla", "pista":"cristal"}
print(diccionario)

print(diccionario["pala"])

diccionario.update({"pala":"dunlop"})
print(diccionario)

print(len(diccionario))

diccionario.clear()
print(diccionario)