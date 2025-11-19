print("Elige un producto del menu:")

print("Menu de Productos:")
print("Producto     Precio")
print("1. Agua       0.50")
print("2. Gaseosa    0.75")
print("3. Zumo       0.95")

print("Pulsa S para salir")
monedas = 0
print("Ingresa monedas para relizar el pago:")
monedas = input("Ingresa las monedas: ")
while monedas == 1 or 2: 
       # print("No se aceptan monedas de 2 cts y 1 cts") 
        monedas = input("Ingresa monedas excepción de los 2 cts y 1 cts")
