# Ejercicio 14
# Crear un algoritmo que pida un número del 1 al 7 y diga el día de la semana
# al que corresponde.

dia_numero = int(input("Introduce un número del 1 al 7 para saber el día de la semana: "))

if dia_numero == 1:
    print("El día correspondiente es Lunes.")
elif dia_numero == 2:
    print("El día correspondiente es Martes.")
elif dia_numero == 3:
    print("El día correspondiente es Miércoles.")
elif dia_numero == 4:
    print("El día correspondiente es Jueves.")
elif dia_numero == 5:
    print("El día correspondiente es Viernes.")
elif dia_numero == 6:
    print("El día correspondiente es Sábado.")
elif dia_numero == 7:
    print("El día correspondiente es Domingo.")
else:
    print("Número no válido. Por favor, introduce un número del 1 al 7.")