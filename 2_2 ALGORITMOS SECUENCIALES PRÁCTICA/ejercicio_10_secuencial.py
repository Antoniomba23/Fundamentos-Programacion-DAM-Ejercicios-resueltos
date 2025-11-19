""" 10. Capturar un número de dos cifras y diseñar un algoritmo que muestre el número
invertido.
Para invertir el número debes obtener las cifras de las decenas y de las unidades
por separado. """

numero = 0
while not ( (10 <= numero <= 99) or (-99 <= numero <= -10) ):
    numero_str = input("Introduce un número de dos cifras: ")
    numero = int(numero_str)
    if not ( (10 <= numero <= 99) or (-99 <= numero <= -10) ):
        print("Por favor, introduce un número que tenga exactamente dos cifras.")


signo = 1
if numero < 0:
    signo = -1
    numero = abs(numero)

decenas = numero // 10
unidades = numero % 10

numero_invertido = (unidades * 10 + decenas) * signo

print(f"El número invertido de {numero * signo} es: {numero_invertido}")