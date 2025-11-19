# Ejercicio 16: N primeros números primos

while True:
    cantidad = int(input("¿Cuántos números primos quieres mostrar? "))
    if cantidad <= 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        break

primos_encontrados = 0
numero_actual = 2
print(f"Los primeros {cantidad} números primos son:")
while primos_encontrados < cantidad:
    # Lógica para verificar si numero_actual es primo
    is_prime = True
    if numero_actual < 2:
        is_prime = False
    else:
        for i in range(2, int(numero_actual**0.5) + 1):
            if numero_actual % i == 0:
                is_prime = False
                break

    if is_prime:
        print(numero_actual)
        primos_encontrados += 1
    numero_actual += 1