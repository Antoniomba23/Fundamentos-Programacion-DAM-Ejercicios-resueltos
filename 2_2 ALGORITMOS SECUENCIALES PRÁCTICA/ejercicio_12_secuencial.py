""" 12.Realiza el algoritmo de un programa que reciba una cantidad de minutos y
muestre por pantalla cuántas horas y minutos son. """

total_minutos = -1
while not (total_minutos >= 0):
    total_minutos_str = input("Introduce una cantidad de minutos: ")
    total_minutos = int(total_minutos_str)
    if not (total_minutos >= 0):
        print("Por favor, introduce un número de minutos no negativo.")

horas = total_minutos // 60
minutos_restantes = total_minutos % 60

print(f"{total_minutos} minutos son {horas} horas y {minutos_restantes} minutos.")