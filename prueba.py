import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('mi_archivo.csv')

# Supongamos que la primera fila contiene las columnas 'Nombre' y 'Apellido'
nombre_apellido = df.loc[4, ['Nombre', 'Edad']]
print(nombre_apellido['Nombre'])
