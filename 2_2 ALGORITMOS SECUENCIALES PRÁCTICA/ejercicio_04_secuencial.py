""" 3. Crear un algoritmo que escriba "Hola" cinco veces. """

suma = 0
for i in range(5):
    numero_valido = False
    while not numero_valido:
        numero_str = input(f"Introduce el número {i+1}: ")
        numero = float(numero_str)
        numero_valido = True # Asumimos que es válido si no hay ValueError
    suma += numero

print(f"La suma de los 5 números es: {suma}")