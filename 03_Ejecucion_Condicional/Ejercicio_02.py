'''
Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones del programa:

Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve
Error, por favor introduzca un número

Introduzca las Horas: cuarenta
Error, por favor introduzca un número
'''

while True:
    try:
        hora = int(input('Introduzca Horas Trabajadas: '))
        break
    except ValueError:
        print('Error, por favor introduzca un número')

while True:
    try:
        tarifa = int(input('Introduzca Tarifa x Hora: '))
        break
    except ValueError:
        print('Error, por favor introduzca un número')


if hora <= 40:
    x = hora * tarifa
    print(f'{x}')
else:
    hora_ext = hora - 40
    pago_ext = (tarifa * hora_ext) * 1.5
    y = (40 * tarifa) + pago_ext
    print(f'{y}')

