'''
Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

Puntuación Calificación
>= 0.9     Sobresaliente
>= 0.8     Notable
>= 0.7     Bien
>= 0.6     Suficiente
< 0.6      Insuficiente
'''

while True:
    try:
        calificacion = float(input('Introduce la calificacion: ')) 
        break       
    except ValueError:
        print('Puntuación incorrecta')
        

if calificacion >= 1 or calificacion < 0:
    print("Puntuación incorrecta")
elif calificacion >= 0.9:
    print("Sobresaliente")
elif calificacion >= 0.8:
    print("Notable")
elif calificacion >= 0.7:
    print("Aceptable")
elif calificacion >= 0.6:
    print("Suficiente")
else:
    print("Insuficiente")

'''
Ejecuta el programa repetidamente, como se muestra arriba, para probar con varios valores de entrada diferentes.

Introduzca puntuación: 0.95
Sobresaliente

Introduzca puntuación: perfecto
Puntuación incorrecta

Introduzca puntuación: 10.0
Puntuación incorrecta

Introduzca puntuación: 0.75
Bien

Introduzca puntuación: 0.5
Insuficiente
'''