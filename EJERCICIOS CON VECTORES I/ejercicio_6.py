# 6. Realizar un programa Java que cargue un vector con las notas de los 40 alumnos de una clase
# y visualice el número de alumnos aprobados, el número de alumnos suspensos y la nota media
# de la clase, y el número de calificaciones superiores a la media.

import random

def ejercicio_6():
    notas = [random.uniform(0.0, 10.0) for _ in range(40)]
    
    aprobados = 0
    suspensos = 0
    suma_notas = 0

    for nota in notas:
        suma_notas += nota
        if nota >= 5.0:
            aprobados += 1
        else:
            suspensos += 1
    
    nota_media = suma_notas / len(notas)

    superiores_media = 0
    for nota in notas:
        if nota > nota_media:
            superiores_media += 1

    print(f"Notas de los alumnos: {notas}")
    print(f"Número de alumnos aprobados: {aprobados}")
    print(f"Número de alumnos suspensos: {suspensos}")
    print(f"Nota media de la clase: {nota_media:.2f}")
    print(f"Número de calificaciones superiores a la media: {superiores_media}")

if __name__ == "__main__":
    ejercicio_6()
