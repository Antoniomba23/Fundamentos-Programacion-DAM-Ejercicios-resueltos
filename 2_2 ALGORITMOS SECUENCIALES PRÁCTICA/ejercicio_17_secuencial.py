""" 17.Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales
30% de la calificación del examen final
15% calificación del trabajo final. """

parcial1 = -1
while not (0 <= parcial1 <= 10):
    parcial1_str = input("Introduce la nota del primer parcial (0-10): ")

    parcial1 = float(parcial1_str)
    if not (0 <= parcial1 <= 10):
        print("La nota debe estar entre 0 y 10.")

parcial2 = -1
while not (0 <= parcial2 <= 10):
    parcial2_str = input("Introduce la nota del segundo parcial (0-10): ")

    parcial2 = float(parcial2_str)
    if not (0 <= parcial2 <= 10):
        print("La nota debe estar entre 0 y 10.")

practicas = -1
while not (0 <= practicas <= 10):
    practicas_str = input("Introduce la nota de prácticas (0-10): ")

    practicas = float(practicas_str)
    if not (0 <= practicas <= 10):
        print("La nota debe estar entre 0 y 10.")

examen_final = -1
while not (0 <= examen_final <= 10):
    examen_final_str = input("Introduce la nota del examen final (0-10): ")

    examen_final = float(examen_final_str)
    if not (0 <= examen_final <= 10):
        print("La nota debe estar entre 0 y 10.")


peso_parcial1 = 0.20
peso_parcial2 = 0.20
peso_practicas = 0.30
peso_examen_final = 0.30

# Calcular la calificación final
calificacion_final = (
    parcial1 * peso_parcial1
    + parcial2 * peso_parcial2
    + practicas * peso_practicas
    + examen_final * peso_examen_final
)

print(f"La calificación final en Algoritmos es: {calificacion_final:.2f}")