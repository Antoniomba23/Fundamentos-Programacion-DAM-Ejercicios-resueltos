from time import sleep  
print ("=== MÁQUINA DE BEBIDAS ===") 
print ("1. Agua (0.50€)") 
print ("2. Gaseosa (0.75€)") 
print ("3. Zumo (0.95€)") 
print ("S. Salir") 
 
opcion = input("Elige una opción: ") 
 
productos = [ "Agua", "Gaseosa", "Zumo"] 
precios = [ 0.50, 0.75, 0.95] 
 
if opcion.upper() == "S": 
   print("Saliendo...") 
   sleep( 3) 
   print("Hasta luego, vuelve pronto!") 
   exit() 
else : 
   opcion = int(opcion) - 1 
   producto_seleccionado = productos[opcion] 
   precio_producto = precios[opcion] 
   print(f"Has elegido {producto_seleccionado} que cuesta {precio_producto:.2f}€") 
 
# ==== Monedas ==== 
monedas_validas = [ 1.00, 0.50, 0.20, 0.10, 0.05] 
monedas = monedas_validas.copy() 
cantidad = [ 20, 20, 20, 20, 20] 
 
# ==== Introducir monedas ==== 
total_introducido = 0 
monedas_introducidas = [] 
 
print (f"Precio a pagar: {precio_producto} €") 
 
while total_introducido < precio_producto: 
   try: 
       moneda = float(input("Introduce una moneda (0.05, 0.10, 0.20, 0.50, 1.00): ")) 
   except ValueError: 
       print("Introduce un número válido.") 
       continue 
 
   if moneda not in monedas_validas: 
       print("Moneda NO aceptada.") 
       continue 
   total_introducido += moneda
   monedas_introducidas.append(moneda) 
   print(f"Total introducido: {total_introducido:.2f}€") 
 
print ("Dinero suficiente.") 
 
# Actualizar monedas introducidas 
for m in monedas_introducidas: 
   pos = monedas.index(m) 
   cantidad[pos] += 1 
 
# ==== Calcular cambio ==== 
# Pasamos a céntimos  
precio_cent = int(precio_producto * 100) 
introducido_cent = int(total_introducido * 100) 
cambio = introducido_cent - precio_cent 
 
cambio_a_dar = [ 0]*len(monedas) 
 
for i in range(len(monedas)): 
   valor_cent = int(monedas[i] * 100) 
   while cambio >= valor_cent and cantidad[i] > 0: 
       cambio -= valor_cent 
       cantidad[i] -= 1 
       cambio_a_dar[i] += 1 
 
# Si no se puede dar cambio exacto 
if cambio > 0: 
   print("\nNo se puede dar cambio exacto.") 
   print("Devolviendo el dinero introducido...") 
   for m in monedas_introducidas: 
       pos = monedas.index(m) 
       cantidad[pos] -= 1 
   print(f"Se han devuelto {total_introducido:.2f}€") 
else : 
   print("\nProducto entregado.") 
   if sum(cambio_a_dar) > 0: 
       print("Cambio entregado:") 
       for i in range(len(monedas)): 
           if cambio_a_dar[i] > 0: 
               print(f"{cambio_a_dar[i]} moneda(s) de {monedas[i]:.2f}€") 
 
# Mostrar total monedas de la máquina 
print ("\nTotal de monedas en la máquina:") 
for i in range(len(monedas)): 
   print(f"{monedas[i]:.2f}€: {cantidad[i]} unidades") 
