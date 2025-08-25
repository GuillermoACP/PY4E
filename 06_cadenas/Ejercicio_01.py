'''
Ejercicio 1: Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
'''
fruta = 'banana'
ultima_letra = len(fruta) - 1
while ultima_letra >= 0:
    letra = fruta[ultima_letra]
    print(letra)
    ultima_letra = ultima_letra - 1