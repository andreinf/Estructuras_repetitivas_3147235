#Ciclo for
#Especialmente para recorrer
#estructuras de datos

#funcion range(python)
#: Crea una lista de numeros en el 
# rango definido por el usuario

numero = int(input("Ingrese un numero:"))

for i in range(1, 11):
    resultado = i * numero
    print(numero, "x", i, "=", resultado)