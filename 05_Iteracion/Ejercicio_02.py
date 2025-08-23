'''
Ejercicio 2: Escribe otro programa que pida una lista de números como la anterior y al final muestre por pantalla el máximo y mínimo de los números, en vez de la media.
'''

def pedir_numeros():
    valores = []
    contador = 0
    suma = 0
    while True:
        entrada = input('Introduzca un número: ')
        
        if entrada.lower() == 'fin':
            break
        try:    
            numero = float(entrada)
            suma = suma + numero
            contador = contador + 1
            valores.append(numero)
            menor = None
            mayor = None
        except ValueError:
            print('Entrada inválida')

        for valor in valores:
            if menor is None or valor < menor:
                menor = valor

        for valor in valores:
            if mayor is None or valor > mayor:
                mayor = valor

    print(f'Suma:{suma}, Contador:{contador}, Menor:{menor}, Mayor:{mayor}')

pedir_numeros()
