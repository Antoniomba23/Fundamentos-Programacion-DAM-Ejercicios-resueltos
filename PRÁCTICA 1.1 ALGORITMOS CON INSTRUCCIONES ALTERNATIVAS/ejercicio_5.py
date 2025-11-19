# Ejercicio 5
# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘género’ y muestre
# el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor
# o igual a dieciocho y el género es ‘F’. En caso de que se cumpla lo mismo,
# pero el sexo sea ‘M’,debe imprimir ‘ACEPTADO’. Si no se cumplen dichas
# condiciones se debe mostrar ‘NO ACEPTADO/A’.

nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
genero = input("Introduce el género (F/M): ").upper()

if nota >= 5 and edad >= 18:
    if genero == 'F':
        print("ACEPTADA")
    elif genero == 'M':
        print("ACEPTADO")
    else:
        print("NO ACEPTADO/A")
else:
    print("NO ACEPTADO/A")