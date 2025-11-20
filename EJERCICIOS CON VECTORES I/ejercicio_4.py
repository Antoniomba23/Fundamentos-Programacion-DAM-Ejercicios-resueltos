# 4. Realizar programa Java que permita cargar un vector numérico de 10 elementos desde teclado
# y, posteriormente visualice la media de los elementos que se encuentran en las posiciones
# pares (0,2,4,…) y la media de los elementos que se encuentran en las posiciones impares(1,
# 3, 5…..) del vector. La tabla sólo debe ser recorrida una vez.

def ejercicio_4():
    vector = []
    # Cargar el vector numérico de 10 elementos
    for i in range(10):
        num = int(input(f"Introduce el elemento {i+1} del vector: "))
        vector.append(num)

    if not vector:
        print("El vector está vacío.")
        return

    sum_pares = 0
    count_pares = 0
    sum_impares = 0
    count_impares = 0

    for i in range(len(vector)):
        if i % 2 == 0:  # Posiciones pares
            sum_pares += vector[i]
            count_pares += 1
        else:  # Posiciones impares
            sum_impares += vector[i]
            count_impares += 1
    
    media_pares = 0
    if count_pares > 0:
        media_pares = sum_pares / count_pares

    medi_impares = 0
    if count_impares > 0:
        medi_impares = sum_impares / count_impares

    print(f"El vector introducido es: {vector}")
    print(f"Media de elementos en posiciones pares: {media_pares:.2f}")
    print(f"Media de elementos en posiciones impares: {medi_impares:.2f}")

if __name__ == "__main__":
    ejercicio_4()
