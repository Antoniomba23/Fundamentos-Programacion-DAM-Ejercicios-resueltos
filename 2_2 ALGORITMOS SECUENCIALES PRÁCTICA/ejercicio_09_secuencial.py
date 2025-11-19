""" 9. Pide al usuario 2 números y muestra la “distancia entre ellos”. (el valor absoluto
de su diferencia). """

numero1_str = input("Introduce el primer número: ")
numero1 = float(numero1_str)

numero2_str = input("Introduce el segundo número: ")
numero2 = float(numero2_str)

distancia = abs(numero1 - numero2)

print(f"La distancia entre {numero1} y {numero2} es: {distancia}")