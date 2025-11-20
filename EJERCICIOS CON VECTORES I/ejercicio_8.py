# 8. Realizar programa Java que permita cargar por teclado un vector numérico TB_NUM[100],
# posteriormente, introducir por teclado una posición, elimine del vector numérico el elemento
# que se encuentre en dicha posición y visualice el vector sin ese elemento.
# Nota: Eliminar un elemento de un vector supone desplazar una posición hacia la izquierda
# el resto de elementos posteriores.

def ejercicio_8():
    tb_num = []
    # Llenar el vector con 100 elementos de ejemplo (0 a 99)
    for i in range(100):
        tb_num.append(i)
    
    print(f"Vector inicial (ejemplo): {tb_num}")

    posicion_a_eliminar = int(input("Introduce la posición del elemento a eliminar (0-99): "))
    while not (0 <= posicion_a_eliminar < len(tb_num)):
        print("Posición inválida. Debe ser un número entre 0 y 99. Inténtalo de nuevo.")
        posicion_a_eliminar = int(input("Introduce la posición del elemento a eliminar (0-99): "))
        
    del tb_num[posicion_a_eliminar]

    print(f"Vector sin el elemento en la posición {posicion_a_eliminar}: {tb_num}")

if __name__ == "__main__":
    ejercicio_8()
