import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
datos = pd.read_csv('argentina_cars_normalizado.csv')

# Verificar si se cargaron bien los datos
print(datos.head())

# Contar la cantidad de autos por marca
conteo_marcas = datos['brand'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
conteo_marcas.plot(kind='bar')
plt.title('Popularidad de las marcas')
plt.xlabel('Marca')
plt.ylabel('Cantidad de autos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
