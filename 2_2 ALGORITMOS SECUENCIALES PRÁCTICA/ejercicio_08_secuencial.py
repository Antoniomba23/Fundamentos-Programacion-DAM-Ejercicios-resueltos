""" 8. Dada una cantidad expresada en pies. Pasar dicho valor a las siguientes medidas:
pulgadas, yardas, metros y a millas por separado. Considere las siguientes
equivalencias: 1 milla = 1609 metros, 1 pulgada = 0.0254 metros, 1 yarda = 3 pies,
1 pie = 12 pulgadas. """

pies = -1.0
while pies < 0:
    pies_str = input("Introduce la cantidad en pies: ")
    pies = float(pies_str)
    if pies < 0:
        print("La cantidad en pies no puede ser negativa.")

# Equivalencias
# 1 pie = 12 pulgadas
# 1 yarda = 3 pies
# 1 pulgada = 0.0254 metros
# 1 milla = 1609 metros

# Convertir pies a pulgadas
pulgadas = pies * 12

# Convertir pies a yardas
yardas = pies / 3

# Convertir pies a metros (pies -> pulgadas -> metros)
metros = pulgadas * 0.0254

# Convertir pies a millas (pies -> pulgadas -> metros -> millas)
millas = metros / 1609

print(f"\n--- Conversiones ---")
print(f"{pies:.2f} pies equivalen a:")
print(f"  {pulgadas:.2f} pulgadas")
print(f"  {yardas:.2f} yardas")
print(f"  {metros:.2f} metros")
print(f"  {millas:.2f} millas")