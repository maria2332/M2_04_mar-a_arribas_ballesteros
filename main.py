#ejercicio 3
num1 = float(input("Introduzca un numero: "))
num2 = float(input("Introduzca otro numero: "))
num3 = float(input("Introduzca otro numero: "))

lista=(num1,num2,num3)
sumatorio = sum(lista)
print("El sumatorio total de la lista es: ",sum(lista))

#ejercicio 4
t_numeros = len(lista)
media = (sumatorio)/t_numeros
print("La media es: ",media)