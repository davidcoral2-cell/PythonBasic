anyoactual = int(input("Dime en qué año estamos: "))
datos = []

for _ in range(4):
    nombre = input("¿Cómo te llamas? ")
    anyodenacimiento = int(input("Dime qué año naciste: "))
    edad = anyoactual - anyodenacimiento
    datos.append((nombre, anyodenacimiento, edad))

print("Any actual{}".format(anyoactual))
print("Nom         \tData naixement\tAnys que farà aquest any")
for nombre, anyodenacimiento, edad in datos:
    print(f"{nombre:<12}\t{anyodenacimiento:<15}\t{edad}")
