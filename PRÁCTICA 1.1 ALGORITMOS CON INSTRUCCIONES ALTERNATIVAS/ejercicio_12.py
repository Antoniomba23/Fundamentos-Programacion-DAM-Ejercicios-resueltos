# Ejercicio 12
# Crear un algoritmo que pida un número y diga cuántas cifras tiene.

numero_str = input("Introduce un número para saber cuántas cifras tiene: ")

# Eliminamos el signo si existe y el punto decimal si es un número flotante
numero_limpio = numero_str.replace("-", "").replace(".", "")

cifras = len(numero_limpio)

print(f"El número {numero_str} tiene {cifras} cifra(s).")