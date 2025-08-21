'''
Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0
'''

hora = int(input('Introduzca Horas Trabajadas: '))
tarifa = int(input('Introduzca Tarifa x Hora: '))

if hora <= 40:
    x = hora * tarifa
    print(f'{x}')
else:
    hora_ext = hora - 40
    pago_ext = (tarifa * hora_ext) * 1.5
    y = (40 * tarifa) + pago_ext
    print(f'{y}')
