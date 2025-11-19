import random

# Ejercicio 10: Adivinar número aleatorio

numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("¡Bienvenido al juego de adivinar el número!")
print("He pensado en un número entre 1 y 100. ¡Intenta adivinarlo!")

while not adivinado:
    intento_usuario = int(input("Introduce tu número: "))
    intentos += 1

    if intento_usuario < 1 or intento_usuario > 100:
        print("Por favor, introduce un número entre 1 y 100.")
    elif intento_usuario < numero_secreto:
        print("El número a adivinar es MAYOR que el que has escrito.")
    elif intento_usuario > numero_secreto:
        print("El número a adivinar es MENOR que el que has escrito.")
    else:
        print(f"¡CORRECTO! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        adivinado = True