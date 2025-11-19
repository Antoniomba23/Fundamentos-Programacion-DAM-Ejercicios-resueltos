"""
Capturar el nombre de un alumno y las calificaciones de tres evaluaciones y
calcula y muestra su nota media final del siguiente modo “La nota media de
<nombre del alumno> es nota”.
"""

num_alumnos = 5
num_notas = 3

suma_total_notas = 0

for i in range(num_alumnos):
    nombre_alumno = input(f"Introduce el nombre del alumno {i+1}: ")
    suma_notas_alumno = 0
    
    for j in range(num_notas):
        nota = float(input(f"Introduce la nota {j+1} para {nombre_alumno}: "))
        suma_notas_alumno += nota
                
    media_alumno = suma_notas_alumno / num_notas
    print(f"La nota media de {nombre_alumno} es: {media_alumno:.2f}")
    suma_total_notas += media_alumno

media_grupo = suma_total_notas / num_alumnos
print(f"\nLa nota media del grupo es: {media_grupo:.2f}")