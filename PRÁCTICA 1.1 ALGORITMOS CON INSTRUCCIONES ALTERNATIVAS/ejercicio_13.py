# Ejercicio 13
# Crear un algoritmo que simule una calculadora básica que realice sumas,
# restas, multiplicaciones y divisiones. El usuario debe introducir dos
# números y la operación que desea realizar.

print("Calculadora Básica")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == '-':
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == '*':
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida. Por favor, introduce +, -, * o /.")