# Ejercicio 9
# Crear un algoritmo que pida 5 números y diga cuál es el menor.

print("Introduce 5 números para encontrar el menor:")

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
numero3 = float(input("Número 3: "))
numero4 = float(input("Número 4: "))
numero5 = float(input("Número 5: "))

menor = numero1

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
if numero4 < menor:
    menor = numero4
if numero5 < menor:
    menor = numero5

print(f"El menor de los 5 números introducidos es: {menor}")