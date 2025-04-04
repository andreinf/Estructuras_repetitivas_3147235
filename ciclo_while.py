# Ejercicio 1
# Imprimir la tabla de multiplicar del
# numero que un usuario ingrese por teclado
# utilizando un ciclo while
#variable contadora
numero = int(input("Ingrese un número: "))
i=10
while i>= 1:
    resultado = numero * i
    print(numero , "x", i, "=", resultado)
    ##instruccion de 
    ##incremento
    i = i - 1