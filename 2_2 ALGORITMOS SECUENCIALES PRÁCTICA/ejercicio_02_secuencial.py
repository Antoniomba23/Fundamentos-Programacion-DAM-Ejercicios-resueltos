""" Vas a capturar el nombre de una persona y el sueldo bruto que va a cobrar. Debes
calcular el sueldo neto de dicha persona. Se le descuenta como IRPF un 12% y en
concepto de Seguridad Social 5’20%. Mostrar un mensaje : El sueldo neto de
xxxxxxxxxx es xxxxxxx euros. """


nombre_persona = input("Introduce el nombre de la persona: ")
sueldo_bruto = float(input("Introduce el sueldo bruto: "))

irpf = sueldo_bruto * 0.12
seguridad_social = sueldo_bruto * 0.0520

sueldo_neto = sueldo_bruto - irpf - seguridad_social

print(f"El sueldo neto de {nombre_persona} es {sueldo_neto:.2f} euros.")