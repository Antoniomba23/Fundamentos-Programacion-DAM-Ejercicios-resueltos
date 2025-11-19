""" 6. Se trata de escribir el algoritmo que permita emitir la factura correspondiente a
una compra de un artículo determinado, del que se adquiere una o varias
unidades.
Se pedirá que se introduzca por teclado el nombre del artículo, el precio unitario
y el nº de unidades que se solicitan.
El IVA a aplicar es del 19%
Muestra por pantalla todos los valores parciales (Precio venta, Iva, precio bruto y
precio final) con sus correspondientes leyendas aclaratorias. """

nombre_articulo = input("Introduce el nombre del artículo: ")

precio_unitario = -1.0
while precio_unitario < 0:
    precio_unitario_str = input("Introduce el precio unitario del artículo: ")
    precio_unitario = float(precio_unitario_str)
    if precio_unitario < 0:
        print("El precio unitario no puede ser negativo.")

unidades = -1
while unidades < 0:
    unidades_str = input("Introduce el número de unidades: ")
    unidades = int(unidades_str)
    if unidades < 0:
        print("El número de unidades no puede ser negativo.")

IVA_PORCENTAJE = 0.19

precio_venta = precio_unitario * unidades
iva = precio_venta * IVA_PORCENTAJE
precio_bruto = precio_venta + iva
precio_final = precio_bruto

print(f"\n--- Factura de Compra ---")
print(f"Artículo: {nombre_articulo}")
print(f"Precio Unitario: {precio_unitario:.2f} euros")
print(f"Unidades: {unidades}")
print(f"-------------------------")
print(f"Precio de Venta (sin IVA): {precio_venta:.2f} euros")
print(f"IVA ({IVA_PORCENTAJE*100:.0f}%): {iva:.2f} euros")
print(f"Precio Bruto: {precio_bruto:.2f} euros")
print(f"Precio Final: {precio_final:.2f} euros")