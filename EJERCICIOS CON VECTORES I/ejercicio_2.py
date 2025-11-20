# 2. A partir de dos vectores numéricos de 15 elementos, denominados vector1 y vector2,
# respectivamente, obtener un tercer vector, vector3 cuyos elementos sean la suma de los
# elementos de los vectores anteriores. Completar los vectores con números comprendidos entre
# 0 y 100, generados aleatoriamente. (Sumar arrays o vectores es sumar elemento a elemento y
# colocar el resultado en la misma posición del vector resultado).

import random

def ejercicio_2():
    vector1 = [random.randint(0, 100) for _ in range(15)]
    vector2 = [random.randint(0, 100) for _ in range(15)]
    vector3 = []

    for i in range(15):
        vector3.append(vector1[i] + vector2[i])

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Vector 3 (suma): {vector3}")

if __name__ == "__main__":
    ejercicio_2()
