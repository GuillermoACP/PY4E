'''
Ejercicio 7: Reescribe el programa de calificaciones del capítulo anterior usando una función llamada calcula_calificacion, que reciba una puntuación como parámetro y devuelva una calificación como cadena.
'''

def calcula_calificacion(puntuacion):
    if puntuacion >= 1 or puntuacion < 0:
        return "Puntuación incorrecta"
    elif puntuacion >= 0.9:
        return "Sobresaliente"
    elif puntuacion >= 0.8:
        return "Notable"
    elif puntuacion >= 0.7:
        return "Aceptable"
    elif puntuacion >= 0.6:
        return "Suficiente"
    else:
        return "Insuficiente"


while True:
    try:
        calificacion = float(input('Introduce la calificacion: ')) 
        break       
    except ValueError:
        print('Puntuación incorrecta')

x = calcula_calificacion(calificacion)
print(x)