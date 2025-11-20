# 5. Hacer un programa que realice las siguientes funciones:
#  1- Llenar un array con las estaturas de los alumnos de una clase (Previamente
# habremos pedido que se introduzca por teclado en número de alumnos de la clase).
#  2- Suma de todas las estaturas de la clase.
#  3- Calculo de la media de estaturas.
#  4- Visualizar cuantos son más altos que la media y cuantos más bajos.

def ejercicio_5():
    estaturas = []
    num_alumnos = 0

    # 1- Llenar un array con las estaturas de los alumnos de una clase
    num_alumnos = int(input("Introduce el número de alumnos en la clase: "))
    while num_alumnos < 0:
        print("El número de alumnos no puede ser negativo. Inténtalo de nuevo.")
        num_alumnos = int(input("Introduce el número de alumnos en la clase: "))

    for i in range(num_alumnos):
        estatura = float(input(f"Introduce la estatura del alumno {i+1} (en metros): "))
        while estatura <= 0:
            print("La estatura debe ser un número positivo. Inténtalo de nuevo.")
            estatura = float(input(f"Introduce la estatura del alumno {i+1} (en metros): "))
        estaturas.append(estatura)

    if not estaturas:
        print("No se introdujeron estaturas.")
        return

    # 2- Suma de todas las estaturas de la clase.
    suma_estaturas = 0
    for estatura in estaturas:
        suma_estaturas += estatura

    # 3- Cálculo de la media de estaturas.
    media_estaturas = 0
    if num_alumnos > 0:
        media_estaturas = suma_estaturas / num_alumnos

    # 4- Visualizar cuantos son más altos que la media y cuantos más bajos.
    mas_altos = 0
    mas_bajos = 0
    for estatura in estaturas:
        if estatura > media_estaturas:
            mas_altos += 1
        elif estatura < media_estaturas:
            mas_bajos += 1
    
    print(f"Estaturas introducidas: {estaturas}")
    print(f"Suma total de estaturas: {suma_estaturas:.2f} metros")
    print(f"Media de estaturas: {media_estaturas:.2f} metros")
    print(f"Alumnos más altos que la media: {mas_altos}")
    print(f"Alumnos más bajos que la media: {mas_bajos}")

if __name__ == "__main__":
    ejercicio_5()
