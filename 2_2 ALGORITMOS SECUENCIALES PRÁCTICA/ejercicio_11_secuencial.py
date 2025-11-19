""" 11. Capturar dos cifras numéricas A y B, y realizar un algoritmo que intercambie el
valor de las citadas variables, mostrando al final el valor de cada una.
 """
A_str = input("Introduce el valor de A: ")
A = float(A_str)

B_str = input("Introduce el valor de B: ")
B = float(B_str)

print(f"Valores originales: A = {A}, B = {B}")

# Intercambiar los valores
temp = A
A = B
B = temp

print(f"Valores intercambiados: A = {A}, B = {B}")