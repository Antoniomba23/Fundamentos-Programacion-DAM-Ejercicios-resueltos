# Ejercicio 11
# Crear un algoritmo que pida tres números y los muestre ordenados de mayor a
# menor.

print("Introduce tres números para ordenarlos de mayor a menor:")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))

# Usamos una lista para facilitar la ordenación
numeros = [num1, num2, num3]

# Ordenamos la lista de mayor a menor
numeros.sort(reverse=True)

print(f"Los números ordenados de mayor a menor son: {numeros[0]}, {numeros[1]}, {numeros[2]}")