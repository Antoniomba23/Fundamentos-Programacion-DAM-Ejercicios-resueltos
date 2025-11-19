# Ejercicio 8: Repasar tablas de multiplicar y contar fallos

while True:
    numero = int(input("Introduce un número para ver su tabla de multiplicar (o 0 para salir): "))
    if numero == 0:
        print("Saliendo del repaso de tablas.")
        break

    fallos = 0
    print(f"\nRepasando la tabla del {numero}:")
    for i in range(1, 11):
        respuesta_correcta = numero * i
        respuesta_usuario = int(input(f"{numero} x {i} = "))

        if respuesta_usuario == respuesta_correcta:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era {respuesta_correcta}.")
            fallos += 1
    
    print(f"Has tenido {fallos} fallo(s) en esta tabla.")
    
    continuar_repaso = input("¿Quieres repasar otra tabla? (s/n): ").lower()
    if continuar_repaso != 's':
        print("Saliendo del repaso de tablas.")
        break