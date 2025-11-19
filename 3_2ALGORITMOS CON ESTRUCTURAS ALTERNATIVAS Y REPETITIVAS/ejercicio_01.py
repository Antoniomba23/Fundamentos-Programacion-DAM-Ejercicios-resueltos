"""
Ejercicio 1
Muestra en pantalla 15 números obtenidos de forma aleatoria. Entre un número y otro
haz que el ordenador espere dos segundos como si estuviera pensando en obtener el
nuevo número.
"""
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

print("\n--- Contador de Números ---")
print("Introduce 10 números enteros.")

for i in range(10):
    numero = int(input(f"Introduce el número {i+1}: "))
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1

print("\n--- Resumen Final ---")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")
print(f"Ceros: {contador_ceros}")




