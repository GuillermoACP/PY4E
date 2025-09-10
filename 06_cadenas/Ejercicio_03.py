'''
Ejercicio 3: Encapsula este código en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
'''

def cuenta(palabra, letra):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            contador = contador + 1
    print(contador)

cuenta("manzana", "a")