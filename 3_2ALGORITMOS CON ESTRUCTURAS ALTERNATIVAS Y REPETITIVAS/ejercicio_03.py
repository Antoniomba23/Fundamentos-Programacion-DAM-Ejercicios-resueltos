# Ejercicio 3: Tabla de multiplicar

while True:
    numero = int(input("Introduce un número entero positivo para ver su tabla de multiplicar (o 0 para salir): "))
    
    if numero == 0:
        print("Saliendo del programa.")
        break
        
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")