'''
Ejercicio 3: Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular el salario bruto.
'''

horas = float(input("Introduce el número de horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
salario_bruto = horas * tarifa
print("El salario bruto es: " + str(salario_bruto))