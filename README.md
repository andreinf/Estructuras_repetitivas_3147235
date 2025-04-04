# Estructuras repetitivas 3147235
Para trabajar ciclos for y while en Python

## Conceptos clave para trabajar  en ciclos

* **Breakpoint(Punto de interrupción)**: Herramienta para ejecutar 
    codigo, una instrucción a la vez.(depuracion - debugger).
    Permite ver el valor de las variales definidas en un programa
    a través de la ejecución de código, permitiendo observar el 
    comportamiento del programa/código a través del tiempo 

* **Variable contadora(contador)**: Variable a la cual podemos
    aumentar (disminuir) su valor en una determinada cantidad
    constante (de 1 en 1, de 2 en 2, etc).

    -Una variable contadora se debe inicializar obligatorio
    **antes de la estrucutra repetitiva** con un valor inicial(0).

    -Una variable contadora, por lo general se nombra con las letras 
     i,j.

    -Una variable contadora **debe participar en la condicional del ciclo**.

    -Toda variable contadora debe tener **instrucción de incremento**
     para aumentar su valor.

    -En un ciclo while, la instrucción de incremento se pone 
     **al final del bloque de codigo del ciclo**

* **Iteración**: Un recorrido en la ejecución de un ciclo.
 
## Ciclo while

Estructura que permite ejecutar un bloque de código un numero determinado de veces.
El bloque de codigo dentro del ciclo while se ejecutara sucesivamente **mientras la condicional sa evaluado como VERDAD**.

### Sintaaxis en python:

```
while condicional: 
      instruccion 1 
      instruccion 2 
      instruccion 3
      ....
      instruccion n

```

## Ciclo for

Se utiliza(Python) para recorrer conjuntos 
de datos(estructuras de datos - colecciones de datos)

* El ciclo recorrera cada dato en la 
estructura desde el primero hasta el ultimo

* El elemento recorrido se asiga a una variable en el 
ciclo

### Sintáxis for:
```
    for <variable> in <conjunto de datos>
        instruccion 1 
        instruccion 2 
        instruccion 3
        ....
        instruccion n

```