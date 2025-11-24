from time import sleep


print("=== MÁQUINA DE BEBIDAS ===")
print("1. Agua (0.50€)")
print("2. Gaseosa (0.75€)")
print("3. Zumo (0.95€)")
print("S. Salir")

opcion = input("Elige una opción: ")

productos = ["Agua", "Gaseosa", "Zumo"]
precios = [0.50, 0.75, 0.95]

# si seleccionamos S de salir
if opcion.upper() == "S":
    print("Saliendo...")
    sleep(3)
    print("Hasta luego, vuelve pronto!")
    exit()
# si el valor seleccionado es distinto de S salir
else:
    opcion = int(opcion) - 1
    producto_seleccionado = productos[opcion]
    precio_producto = precios[opcion]
    print(f"Has elegido {producto_seleccionado} que cuesta {precio_producto}€")

# ==== Monedas ====
monedas_validas = [1.00, 0.50, 0.20, 0.10, 0.05]
monedas = monedas_validas.copy()
cantidad = [20, 20, 20, 20, 20]  # cantidad de monedas en la máquina

# ==== Comprobar modo exacto ====
tipos_disponibles = sum(1 for c in cantidad if c > 0) #
modo_exacto = tipos_disponibles < 2 or (cantidad[:-1].count(0) == 4 and cantidad[-1] > 0)
if modo_exacto:
    print("\n*** INTRODUZCA IMPORTE EXACTO ***")

# ==== Introducir monedas ====
total_introducido = 0
monedas_introducidas = []

print(f"Precio a pagar: {precio_producto} €")

while total_introducido < precio_producto:
    try:
        moneda = float(input("Introduce una moneda (0.05, 0.10, 0.20, 0.50, 1.00): "))
    except ValueError:
        print("Introduce un número válido.")
        continue

    if moneda not in monedas_validas:
        print("Moneda NO aceptada. No se admiten 1ct, 2cts ni monedas no válidas.")
        continue

    # Modo exacto: no permitir superar el precio
    if modo_exacto and total_introducido + moneda > precio_producto:
        print("Excede el precio. Introduzca importe exacto.")
        continue

    total_introducido += moneda
    monedas_introducidas.append(moneda)
    round(total_introducido, 3)
    print(f"Total introducido: {total_introducido}€")

print("Dinero suficiente.")

# Actualizar monedas introducidas
for m in monedas_introducidas:
    total = monedas.index(m)
    cantidad[total] += 1

#  Calcular cambio si NO es modo exacto
if not modo_exacto:
    cambio = round(total_introducido - precio_producto, 2)
    cambio_a_dar = [0]*len(monedas)

    for i in range(len(monedas)):
        while cambio >= monedas[i] and cantidad[i] > 0:
            cambio -= monedas[i]
            cantidad[i] -= 1
            cambio_a_dar[i] += 1

    if sum(cambio_a_dar) == 0 and cambio > 0:
        print("\nNo se puede dar cambio exacto.")
    elif sum(cambio_a_dar) > 0:
        print("\nCambio entregado:")
        for i in range(len(monedas)):
            if cambio_a_dar[i] > 0:
                print(f"{cambio_a_dar[i]} moneda(s) de {monedas[i]}€")

#  Mostrar total monedas de la máquina
print("\nTotal de monedas en la máquina:")
for i in range(len(monedas)):
    print(f"{monedas[i]}€: {cantidad[i]} unidades")
