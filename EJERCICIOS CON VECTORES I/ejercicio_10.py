# 10. Realizar un programa Java que pida un número entero positivo de 10 cifras, y que compruebe
# si el número es capicúa

def ejercicio_10():
    numero_str = input("Introduce un número entero positivo de 10 cifras: ")
    while not (numero_str.isdigit() and len(numero_str) == 10 and int(numero_str) > 0):
        print("Entrada inválida. Debe ser un número entero positivo de 10 cifras. Inténtalo de nuevo.")
        numero_str = input("Introduce un número entero positivo de 10 cifras: ")

    # Comprobar si el número es capicúa
    numero_invertido_str = ""
    for i in range(len(numero_str) - 1, -1, -1):
        numero_invertido_str += numero_str[i]

    es_capicua = (numero_str == numero_invertido_str)

    print(f"Número introducido: {numero_str}")
    if es_capicua:
        print("El número es capicúa.")
    else:
        print("El número NO es capicúa.")

if __name__ == "__main__":
    ejercicio_10()
