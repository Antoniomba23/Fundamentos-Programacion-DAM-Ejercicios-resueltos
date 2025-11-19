# Ejercicio 12: Intervalo de números

while True:
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))

    if limite_inferior > limite_superior:
        print("Error: El límite inferior no puede ser mayor que el límite superior. Inténtalo de nuevo.")
    else:
        break

suma_dentro_intervalo = 0
numeros_fuera_intervalo = 0
igual_a_limites = False

print(f"Introduce números (0 para terminar). El intervalo es ({limite_inferior}, {limite_superior}).")

while True:
    numero = int(input("Introduce un número: "))
    if numero == 0:
        break

    if limite_inferior < numero < limite_superior:
        suma_dentro_intervalo += numero
    else:
        numeros_fuera_intervalo += 1
    
    if numero == limite_inferior or numero == limite_superior:
        igual_a_limites = True

print("\n--- Resultados del análisis del intervalo ---")
print(f"Suma de los números dentro del intervalo ({limite_inferior}, {limite_superior}): {suma_dentro_intervalo}")
print(f"Cantidad de números fuera del intervalo: {numeros_fuera_intervalo}")
if igual_a_limites:
    print("Se introdujo al menos un número igual a los límites del intervalo.")
else:
    print("No se introdujo ningún número igual a los límites del intervalo.")