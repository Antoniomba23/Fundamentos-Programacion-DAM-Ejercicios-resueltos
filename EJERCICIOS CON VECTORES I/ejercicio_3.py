# 3. Realizar un programa Java que inicialice un array numérico de 10 elementos y visualizar los
# elementos que sean par y la posición en que se encuentra.

import random

def ejercicio_3():
    # Inicializar un array numérico de 10 elementos con números aleatorios para simular carga
    array_numerico = [random.randint(1, 100) for _ in range(10)]
    print(f"Array numérico: {array_numerico}")
    print("Elementos pares y sus posiciones:")
    for i in range(len(array_numerico)):
        if array_numerico[i] % 2 == 0:
            print(f"  Elemento: {array_numerico[i]}, Posición: {i}")

if __name__ == "__main__":
    ejercicio_3()
