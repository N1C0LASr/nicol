import pandas as pd

data = {
    'Nombre': ['Ana', 'Juan', 'María', 'Carlos', 'Luisa', 'Pedro', 'Laura', 'Miguel', 'Sofía', 'Diego',
               'Valentina', 'Andrés', 'Camila', 'Alejandro', 'Lucía', 'Gabriel', 'Isabella', 'Javier', 'Emma', 'Daniel'],
    'Edad': [25, 32, 19, 45, 28, 36, 21, 39, 30, 33, 27, 24, 31, 41, 20, 29, 22, 37, 26, 34]
}

df = pd.DataFrame(data)
nombre_archivo = 'name and date.csv'
df.to_csv(nombre_archivo, index=False)