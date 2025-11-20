# 1. Realizar programa Java que permita cargar un vector numérico de 10 elementos desde teclado
# y, posteriormente visualice el valor del elemento mayor y cuántas veces se repite en el vector
# este valor máximo. Utiliza JOptionPane.

def ejercicio_1():
    vector = []
    # Cargar el vector numérico de 10 elementos
    for i in range(10):
        num = int(input(f"Introduce el elemento {i+1} del vector: "))
        vector.append(num)

    if not vector:
        print("El vector está vacío.")
        return

    # Visualizar el valor del elemento mayor
    max_valor = vector[0] 
    for num in vector:
        if num > max_valor:
            max_valor = num
    
    # Contar cuántas veces se repite el valor máximo
    count_max_valor = 0
    for num in vector:
        if num == max_valor:
            count_max_valor += 1

    print(f"El vector introducido es: {vector}")
    print(f"El valor del elemento mayor es: {max_valor}")
    print(f"El valor máximo se repite {count_max_valor} veces.")

if __name__ == "__main__":
    ejercicio_1()
