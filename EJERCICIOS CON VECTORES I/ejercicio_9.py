# 9. Crear un programa que lea por teclado un número entero y que almacene el mismo en un
# array de modo que cada cifra ocupe un elemento del array. Ejemplo: si leo el número
# 23451, se generará el array:    I 2I 3I 4I 5I 1I

def ejercicio_9():
    numero_str = input("Introduce un número entero: ")
            
    # Convertir el número en un array de cifras
    array_cifras = []
    for digito in numero_str:
        array_cifras.append(int(digito))

    print(f"Número introducido: {numero_str}")
    print(f"Array de cifras: {array_cifras}")

if __name__ == "__main__":
    ejercicio_9()
