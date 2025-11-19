# Capturar el nombre de un alumno y las calificaciones de tres evaluaciones y
# calcula y muestra su nota media final del siguiente modo “La nota media de
# <nombre del alumno> es nota”.


nombre_alumno = input("Introduce el nombre del alumno: ")

calificacion1 = float(input("Introduce la calificación de la primera evaluación: "))
calificacion2 = float(input("Introduce la calificación de la segunda evaluación: "))
calificacion3 = float(input("Introduce la calificación de la tercera evaluación: "))

nota_media = (calificacion1 + calificacion2 + calificacion3) / 3

print(f"La nota media de {nombre_alumno} es {nota_media:.2f}")