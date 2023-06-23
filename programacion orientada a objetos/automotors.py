import pandas as pd

class RegistroVentas:
    def __init__(self, archivo):
        self.df = pd.read_csv(archivo)
    
    def ver_datos(self):
        print(self.df)
    
    def modificar_registro(self, indice, columna, nuevo_valor):
        self.df.loc[indice, columna] = nuevo_valor
    
    def agregar_registro(self, datos):
        nuevo_registro = pd.DataFrame([datos], columns=self.df.columns)
        self.df = pd.concat([self.df, nuevo_registro], ignore_index=True)
    
    def guardar_datos(self, archivo):
        self.df.to_csv(archivo, index=False)

# Archivo principal
nombre_archivo = 'prototipo_dt_automotors.csv'
registro = RegistroVentas(nombre_archivo)

# Opción 1: Ver datos
registro.ver_datos()

# Opción 2: Modificar registros
registro.modificar_registro(indice=0, columna='Tipo', nuevo_valor='Venta')
registro.ver_datos()

# Opción 3: Agregar registros
nuevo_registro = {'Fecha': '2023-06-10', 'Tipo': 'Arriendo', 'Vehículo': 'Ford Fiesta', 'Cliente': 'Cliente G', 'Precio': 70000}
registro.agregar_registro(nuevo_registro)
registro.ver_datos()

# Guardar los cambios en el archivo
registro.guardar_datos(nombre_archivo)