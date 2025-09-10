'''
Ejercicio 4: Hay un método de cadenas llamado count que es similar a la función del ejercicio previo. Lee la documentación de este método en:

https://docs.python.org/library/stdtypes.html#string-methods

Escribe una invocación que cuenta el número de veces que una letra aparece en “banana”.
'''

def cuenta(palabra, letra):
    contador = palabra.count(letra)
    print(contador)

cuenta("manzana", "a")
cuenta("banana", "a")