# Ejercicio 8
# Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el
# usuario. Si se introduce un número negativo, debe mostrar un mensaje de
# error.

import math

numero = float(input("Introduce un número para calcular su raíz cuadrada: "))

if numero >= 0:
    raiz_cuadrada = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
else:
    print("Error: No se puede calcular la raíz cuadrada de un número negativo.")