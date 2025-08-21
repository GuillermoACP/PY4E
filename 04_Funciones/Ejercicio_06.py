'''
Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-y-media para las horas extras, y crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa).

Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0
'''

def calculo_salario(hora, tarifa):
    if hora <= 40:
        salario = hora * tarifa
    else:
        hora_ext = hora - 40
        pago_ext = (tarifa * hora_ext) * 1.5
        salario = (40 * tarifa) + pago_ext

    return salario


while True:
    try:
        hora = int(input('Introduzca Horas Trabajadas: '))
        break
    except ValueError:
        print('Error, por favor introduzca un número valido')

while True:
    try:
        tarifa = int(input('Introduzca Tarifa x Hora: '))
        break
    except ValueError:
        print('Error, por favor introduzca un número valido')

x = calculo_salario(hora, tarifa)
print("Salario:", x)
