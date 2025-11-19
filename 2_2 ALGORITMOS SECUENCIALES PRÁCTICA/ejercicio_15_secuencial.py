""" 15.Escribir un algoritmo para calcular la nota final de un estudiante en un test a
partir de las respuestas correctas, incorrectas y en blanco, considerando que,
cada respuesta correcta vale 1 punto, cada incorrecta resta 0,25 y las respuestas
en blanco valen 0. """

nota1 = -1.0
while not (0 <= nota1 <= 10):
    nota1_str = input("Introduce la nota del primer test (0-10): ")
    nota1 = float(nota1_str)
    if not (0 <= nota1 <= 10):
        print("La nota debe estar entre 0 y 10.")

nota2 = -1.0
while not (0 <= nota2 <= 10):
    nota2_str = input("Introduce la nota del segundo test (0-10): ")
    nota2 = float(nota2_str)
    if not (0 <= nota2 <= 10):
        print("La nota debe estar entre 0 y 10.")

nota3 = -1.0
while not (0 <= nota3 <= 10):
    nota3_str = input("Introduce la nota del tercer test (0-10): ")
    nota3 = float(nota3_str)
    if not (0 <= nota3 <= 10):
        print("La nota debe estar entre 0 y 10.")

# Calcular la nota final (promedio simple)
nota_final = (nota1 + nota2 + nota3) / 3

print(f"La nota final del estudiante es: {nota_final:.2f}")