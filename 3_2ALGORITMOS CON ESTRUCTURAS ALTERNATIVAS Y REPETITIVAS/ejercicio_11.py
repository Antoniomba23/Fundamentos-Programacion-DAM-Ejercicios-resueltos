# Ejercicio 11: Convertir decimal a binario

while True:
    decimal = int(input("Introduce un número decimal positivo para convertir a binario: "))
    if decimal < 0:
        print("Por favor, introduce un número positivo.")
    elif decimal == 0:
        print("El número 0 en binario es: 0")
        break
    else:
        binario = ""
        temp_decimal = decimal
        while temp_decimal > 0:
            binario = str(temp_decimal % 2) + binario
            temp_decimal //= 2
        print(f"El número {decimal} en binario es: {binario}")
        break