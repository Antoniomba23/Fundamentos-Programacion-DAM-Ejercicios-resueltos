# Ejercicio 10
# Crear un algoritmo que pida números hasta que se introduzca un negativo, y
# en ese momento, que muestre el mayor y el menor de los números introducidos.

mayor = float('-inf')  # Inicializar con el valor negativo más pequeño posible
menor = float('inf')   # Inicializar con el valor positivo más grande posible

primer_numero = True

while True:
    numero = float(input("Introduce un número (introduce un número negativo para terminar): "))

    if numero < 0:
        break

    if primer_numero:
        mayor = numero
        menor = numero
        primer_numero = False
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

if primer_numero: # Si no se introdujo ningún número positivo
    print("No se introdujeron números positivos.")
else:
    print(f"El mayor de los números introducidos es: {mayor}")
    print(f"El menor de los números introducidos es: {menor}")