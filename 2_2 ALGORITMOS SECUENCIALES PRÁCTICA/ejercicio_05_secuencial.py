""" 5. Crear un algoritmo que calcule la raíz cuadrada del número que introduzca el
usuario. Comprobar qué pasa si introduzca un número negativo. """

import math

numero = -1.0
while numero < 0:
    numero_str = input("Introduce un número para calcular su raíz cuadrada: ")
    numero = float(numero_str)
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo en los números reales.")

raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")