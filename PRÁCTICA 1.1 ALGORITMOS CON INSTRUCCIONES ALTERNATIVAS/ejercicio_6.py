# Ejercicio 6
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las
# dimensiones de los lados de un triángulo. El programa debe determinar que
# tipo de triangulo es, teniendo en cuenta los siguiente:
# • Si se cumple Pitágoras entonces es triángulo rectángulo
# • Si sólo dos lados del triángulo son iguales entonces es isósceles.
# • Si los 3 lados son iguales entonces es equilátero.
# • Si no se cumple ninguna de las condiciones anteriores, es escaleno.

lado_a = float(input("Introduce la longitud del lado A: "))
lado_b = float(input("Introduce la longitud del lado B: "))
lado_c = float(input("Introduce la longitud del lado C: "))

# Comprobar si es un triángulo válido
if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
    print("No es un triángulo válido.")
# Comprobar si es equilátero
elif lado_a == lado_b and lado_b == lado_c:
    print("Es un triángulo equilátero.")
# Comprobar si es isósceles
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print("Es un triángulo isósceles.")
# Comprobar si es rectángulo (usando el teorema de Pitágoras)
elif (lado_a**2 + lado_b**2 == lado_c**2) or \
     (lado_a**2 + lado_c**2 == lado_b**2) or \
     (lado_b**2 + lado_c**2 == lado_a**2):
    print("Es un triángulo rectángulo.")
# Si no es ninguno de los anteriores, es escaleno
else:
    print("Es un triángulo escaleno.")