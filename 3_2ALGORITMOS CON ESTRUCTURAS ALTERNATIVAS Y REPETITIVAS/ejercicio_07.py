# Ejercicio 7: Repasar tablas de multiplicar continuamente

while True:
    numero = int(input("Introduce un número para ver su tabla de multiplicar (o 0 para salir): "))
    if numero == 0:
        print("Saliendo del repaso de tablas.")
        break

    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    
    continuar_repaso = input("¿Quieres repasar otra tabla? (s/n): ").lower()
    if continuar_repaso != 's':
        print("Saliendo del repaso de tablas.")
        break