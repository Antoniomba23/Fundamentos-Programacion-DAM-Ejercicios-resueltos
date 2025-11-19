""" 13.Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un
algoritmo que determine la hora de llegada a la ciudad B.
Sugerencia: convierte la hora de salida toda a segundos. """

horas_salida = -1
while not (0 <= horas_salida < 24):
    horas_salida_str = input("Introduce la hora de salida (HH): ")
    horas_salida = int(horas_salida_str)
    if not (0 <= horas_salida < 24):
        print("La hora debe estar entre 0 y 23.")

minutos_salida = -1
while not (0 <= minutos_salida < 60):
    minutos_salida_str = input("Introduce los minutos de salida (MM): ")
    minutos_salida = int(minutos_salida_str)
    if not (0 <= minutos_salida < 60):
        print("Los minutos deben estar entre 0 y 59.")

segundos_salida = -1
while not (0 <= segundos_salida < 60):
    segundos_salida_str = input("Introduce los segundos de salida (SS): ")
    segundos_salida = int(segundos_salida_str)
    if not (0 <= segundos_salida < 60):
        print("Los segundos deben estar entre 0 y 59.")

# Capturar el tiempo de viaje en segundos
tiempo_viaje_segundos = -1
while not (tiempo_viaje_segundos >= 0):
    tiempo_viaje_segundos_str = input("Introduce el tiempo de viaje en segundos (T): ")
    tiempo_viaje_segundos = int(tiempo_viaje_segundos_str)
    if not (tiempo_viaje_segundos >= 0):
        print("El tiempo de viaje no puede ser negativo.")

# Convertir la hora de salida a segundos totales
segundos_totales_salida = horas_salida * 3600 + minutos_salida * 60 + segundos_salida

# Calcular los segundos totales de llegada
segundos_totales_llegada = segundos_totales_salida + tiempo_viaje_segundos

# Ajustar para el formato de 24 horas si se excede un día
segundos_totales_llegada %= (24 * 3600)

# Convertir los segundos totales de llegada a HH, MM, SS
horas_llegada = segundos_totales_llegada // 3600
segundos_restantes = segundos_totales_llegada % 3600
minutos_llegada = segundos_restantes // 60
segundos_llegada = segundos_restantes % 60

print(f"La hora de llegada a la ciudad B es: {horas_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}")