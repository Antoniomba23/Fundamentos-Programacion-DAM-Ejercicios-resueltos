# Ejercicio 13: Potencia sin operador

while True:
    base = float(input("Introduce la base (número real): "))
    exponente = int(input("Introduce el exponente (entero positivo): "))

    if exponente < 0:
        print("El exponente debe ser un entero positivo. Inténtalo de nuevo.")
    else:
        break

resultado = 1
for _ in range(exponente):
    resultado *= base

print(f"El resultado de {base} elevado a {exponente} es: {resultado}")