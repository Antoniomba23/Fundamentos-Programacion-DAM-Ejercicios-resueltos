""" 7. Resuelve una ecuación de segundo grado a partir de sus coeficientes.
 """
import math

print("Resolver una ecuación de segundo grado: ax^2 + bx + c = 0")

# Nota: Si el usuario introduce un valor no numérico, el programa generará un ValueError y se detendrá.

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("La ecuación tiene infinitas soluciones (0 = 0).")
        else:
            print("La ecuación no tiene solución (c != 0).")
    else:
        x = -c / b
        print(f"La ecuación es lineal y tiene una solución: x = {x:.2f}")
else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"La ecuación tiene dos soluciones reales distintas:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una solución real doble: x = {x:.2f}")
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2*a)
        print(f"La ecuación tiene dos soluciones complejas conjugadas:")
        print(f"x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i")
        print(f"x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i")