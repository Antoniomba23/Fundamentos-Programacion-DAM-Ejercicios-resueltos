# Ejercicio 3
# Crea un programa que pida al usuario dos números y muestre su división si el
# segundo no es cero, o un mensaje de aviso en caso contrario.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} entre {numero2} es: {division}")
else:
    print("No se puede dividir por cero.")