# Ejercicio 14: Menú de opciones

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    print("------------------------")

    seleccion = int(input("Introduce el número de tu opción: "))

    if seleccion == 1:
        print("Has seleccionado la Opción 1.")
    elif seleccion == 2:
        print("Has seleccionado la Opción 2.")
    elif seleccion == 3:
        print("Has seleccionado la Opción 3.")
    elif seleccion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")