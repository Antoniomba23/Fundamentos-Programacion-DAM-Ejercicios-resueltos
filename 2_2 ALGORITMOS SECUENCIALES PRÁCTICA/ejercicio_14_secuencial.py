""" 14.Pedir el nombre y los dos apellidos de una persona y mostrar sus iniciales
separadas por puntos. """

nombre = input("Introduce el nombre: ").strip()
apellido1 = input("Introduce el primer apellido: ").strip()
apellido2 = input("Introduce el segundo apellido: ").strip()

inicial_nombre = nombre[0].upper() if nombre else ''
inicial_apellido1 = apellido1[0].upper() if apellido1 else ''
inicial_apellido2 = apellido2[0].upper() if apellido2 else ''

iniciales = []
if inicial_nombre:
    iniciales.append(inicial_nombre)
if inicial_apellido1:
    iniciales.append(inicial_apellido1)
if inicial_apellido2:
    iniciales.append(inicial_apellido2)

print("Las iniciales son: " + ".".join(iniciales) + ".")