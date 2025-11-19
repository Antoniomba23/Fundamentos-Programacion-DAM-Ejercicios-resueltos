# Ejercicio 6: Contar números por grupos y continuar

contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

print("\n--- Contador de Números por Grupos ---")

while True:
    numero = float(input("Introduce un número (o 's' para salir): "))

    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1

    continuar = input("¿Quieres introducir otro número? (s/n): ").lower()
    if continuar != 's':
        break

print("\n--- Resumen Final ---")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")
print(f"Ceros: {contador_ceros}")