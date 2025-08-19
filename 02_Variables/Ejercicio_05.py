'''
Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
'''
print('Convertidor de C° a F°')
t_celcius = float (input ('Escribe la temperatura en C°: '))
t_fahren = (t_celcius * (9/5)) + 32

print (f'La temperatura F° es: {t_fahren}')