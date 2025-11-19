# Ejercicio 15: Número primo

num = int(input("Introduce un número entero para verificar si es primo: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"El número {num} ES primo.")
else:
    print(f"El número {num} NO es primo.")