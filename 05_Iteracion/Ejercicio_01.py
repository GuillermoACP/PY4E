'''
Ejercicio 1: Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, detecta su fallo usando try y except, muestra un mensaje de error y pasa al número siguiente.
'''

def pedir_numeros():
    contador = 0
    suma = 0
    while True:
        entrada = input('Numero: ')
        
        if entrada.lower() == 'fin':
            break
        try:    
            numero = float(entrada)
            suma = suma + numero
            contador = contador + 1
            media = suma / contador
        except ValueError:
            print('Introduzca un numero')

    print(suma, contador, media)

pedir_numeros()



'''
Introduzca un número: 4
Introduzca un número: 5
Introduzca un número: dato erróneo
Entrada inválida
Introduzca un número: 7
Introduzca un número: fin
16 3 5.33333333333
'''