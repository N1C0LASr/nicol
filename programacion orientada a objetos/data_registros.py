import pandas as pd

data = {
    'Registro': [
        '2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05', '2023-06-06', '2023-06-07',
        '2023-06-08', '2023-06-09'
    ],
    'Vehiculos': [
        'Toyota Camry', 'Honda Civic', 'Chevrolet Spark', 'Nissan Sentra', 'Ford Mustang', 'Volkswagen Golf',
        'Hyundai Elantra', 'Kia Sportage', 'Mazda CX-5'
    ],
    'Tipo': [
        'Arriendo', 'Arriendo', 'Arriendo', 'Venta', 'Venta', 'Venta', 'Adquisición', 'Adquisición', 'Adquisición'
    ],
    'Clientes': [
        'Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E', 'Cliente F', 'Proveedor X',
        'Proveedor Y', 'Proveedor Z'
    ],
    'Precios': [
        100000, 80000, 60000, 200000, 300000, 150000, 180000, 220000, 250000
    ]
}

df = pd.DataFrame(data)
nombre_archivo = 'prototipo_dt_automotors.csv'
df.to_csv(nombre_archivo, index=False)
