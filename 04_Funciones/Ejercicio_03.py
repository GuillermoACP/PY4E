'''
Ejercicio 3: Desplaza la llamada de la función de nuevo hacia el final, y coloca la definición de muestra_estribillo después de la definición de repite_estribillo. ¿Qué ocurre cuando haces funcionar ese programa?
'''

def muestra_estribillo():
    print('Soy un leñador, que alegría.')
    print('Duermo toda la noche y trabajo todo el día.')

def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()

repite_estribillo()
muestra_estribillo()