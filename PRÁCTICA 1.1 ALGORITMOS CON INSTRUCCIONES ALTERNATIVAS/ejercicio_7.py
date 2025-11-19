# Ejercicio 7
# Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es
# bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto
# que también sea divisible por 400.

ano = int(input("Introduce un año: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")