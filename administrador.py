import csv

# Define los nombres de las columnas
column_names = ['Nombre', 'Edad', 'Correo']

# Abre el archivo CSV en modo escritura
with open('mi_archivo.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escribe los encabezados en la primera fila
    writer.writerow(column_names)

    # Puedes agregar filas de datos aquí
    writer.writerow(['Ana', 30, 'ana@example.com'])
    writer.writerow(['Juan', 25, 'juan@example.com'])
