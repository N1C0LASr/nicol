# Crear un diccionario vacío para almacenar la información de los estudiantes
Padawans = {}

# Iterar 3 veces para ingresar los datos de cada estudiante
for i in range(3):
    # Pedir al usuario que ingrese la información
    nombre = input("Ingrese el nombre del Padawan: ")
    asignatura = input("Ingrese el nombre de la asignatura: ")
    nota_lab1 = float(input("Ingrese la nota del Laboratorio N°1: "))
    nota_lab2 = float(input("Ingrese la nota del Laboratorio N°2: "))

    # Calcular el promedio ponderado
    promedio = (nota_lab1 * 0.3) + (nota_lab2 * 0.7)

    # Crear un diccionario para almacenar la información del estudiante actual
    Padawan  = {
        "Nombre": nombre,
        "Asignatura": asignatura,
        "Nota Laboratorio N°1": nota_lab1,
        "Nota Laboratorio N°2": nota_lab2,
        "Promedio Final": round(promedio, 1)  # Redondear el promedio a 1 decimal
    }

    # Agregar el diccionario del estudiante al diccionario general de estudiantes
    Padawans [i + 1] = Padawan 

# Imprimir la información de todos los estudiantes
for Padawan_num, Padawan_info in Padawans .items():
    print("\nInformación del estudiante", Padawan_num)
    for key, value in Padawan_info.items():
        print(key + ":", value)
