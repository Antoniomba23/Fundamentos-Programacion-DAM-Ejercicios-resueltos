# Ejercicio 1
# Crear un algoritmo que pida al usuario un número y le diga si es positivo, negativo o cero.

numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")