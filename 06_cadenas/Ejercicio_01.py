'''
Ejercicio 1: Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
'''

def hacia_atras():
    while True:
        palabra = input ('Escribe una palabra o FIN para terminar:')
        if palabra.lower() == "fin":
            break
        ultima_letra = len(palabra) -1
        while ultima_letra >= 0:
            letra = palabra[ultima_letra]
            print(letra)
            ultima_letra = ultima_letra - 1
            
        
hacia_atras()