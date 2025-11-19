# Ejercicio 5: Cálculo de sueldos e impuestos

total_irpf_recaudado = 0
total_seguridad_social_recaudada = 0
total_dinero_empresa_bruto = 0

# Tasas de impuestos (ejemplo simplificado, pueden ajustarse)
TAZA_IRPF = 0.15  # 15%
TAZA_SEGURIDAD_SOCIAL_EMPLEADO = 0.06 # 6% del empleado
TAZA_SEGURIDAD_SOCIAL_EMPRESA = 0.25 # 25% de la empresa (contribución adicional)

print("\n--- Cálculo de Sueldos e Impuestos ---")
print("Introduce un sueldo positivo para continuar. Introduce un número negativo para terminar.")

while True:
    sueldo_bruto = float(input("Introduce el sueldo bruto del trabajador (o negativo para salir): "))

    if sueldo_bruto < 0:
        break

    # Cálculos individuales
    irpf = sueldo_bruto * TAZA_IRPF
    seguridad_social_empleado = sueldo_bruto * TAZA_SEGURIDAD_SOCIAL_EMPLEADO
    sueldo_neto = sueldo_bruto - irpf - seguridad_social_empleado
    seguridad_social_empresa = sueldo_bruto * TAZA_SEGURIDAD_SOCIAL_EMPRESA
    costo_total_empresa = sueldo_bruto + seguridad_social_empresa

    print(f"\nSueldo Bruto: {sueldo_bruto:.2f}€")
    print(f"IRPF ({TAZA_IRPF*100:.0f}%): {irpf:.2f}€")
    print(f"Seguridad Social Empleado ({TAZA_SEGURIDAD_SOCIAL_EMPLEADO*100:.0f}%): {seguridad_social_empleado:.2f}€")
    print(f"Sueldo Neto: {sueldo_neto:.2f}€")
    print(f"Costo total para la empresa (incl. SS empresa {TAZA_SEGURIDAD_SOCIAL_EMPRESA*100:.0f}%): {costo_total_empresa:.2f}€")

    # Acumular totales
    total_irpf_recaudado += irpf
    total_seguridad_social_recaudada += (seguridad_social_empleado + seguridad_social_empresa)
    total_dinero_empresa_bruto += costo_total_empresa

print("\n--- Resumen Final ---")
print(f"Dinero total recaudado por el Estado (IRPF): {total_irpf_recaudado:.2f}€")
print(f"Dinero total recaudado por el Estado (Seguridad Social): {total_seguridad_social_recaudada:.2f}€")
print(f"Dinero total pagado por la empresa (antes de impuestos): {total_dinero_empresa_bruto:.2f}€")