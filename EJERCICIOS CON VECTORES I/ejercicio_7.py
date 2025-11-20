# 7. Realizar un programa Java que permita cargar por teclado un vector numérico TB_NUM[100],
# posteriormente, introducir un valor desde teclado e intercalarlo en su posición correcta dentro
# del vector numérico supuestamente ordenado, y visualice finalmente el vector con el dato
# intercalado. El valor antiguo que estaba en la posición en la que se inserta se pierde.

def ejercicio_7():
    tb_num = []
    # Llenar el vector con 100 elementos de forma ordenada (ejemplo)
    for i in range(100):
        tb_num.append(i * 2)
    
    print(f"Vector inicial (ejemplo): {tb_num}")

    valor_intercalar = int(input("Introduce un valor entero para intercalar: "))

    # Buscar la posición correcta para intercalar el valor
    posicion_insercion = 0
    for i in range(len(tb_num)):
        if tb_num[i] > valor_intercalar:
            posicion_insercion = i
            break
    else:
        posicion_insercion = len(tb_num) 

    # Intercalar el valor (sustituyendo el valor antiguo)
    if posicion_insercion < len(tb_num):
        tb_num[posicion_insercion] = valor_intercalar
    else:
        tb_num.append(valor_intercalar)

    print(f"Vector con el dato intercalado: {tb_num}")

if __name__ == "__main__":
    ejercicio_7()
