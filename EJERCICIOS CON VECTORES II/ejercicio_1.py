carton = []

for i in range(4):
    boleto = []
    print(f"Boleto {i+1}:")
    for i in range(8):
        apuesta = int(input(f"Introduce el numero de 1 al 49: "))
        while apuesta in boleto:
            apuesta = int(input(f"Introduce un numero no escogido en este boleto (1-9): "))
        boleto.append(apuesta)
        
    carton.append(boleto)
print(carton)
    