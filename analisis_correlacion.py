import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datos = pd.read_csv("argentina_cars_normalizado.csv")

# Filtrar solo las columnas numéricas
datos_numericos = datos.select_dtypes(include=['number'])

# Calcular correlación
corr = datos_numericos.corr()

# Graficar
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Correlaciones')
plt.show()

#ver pesos y dolares, columna un....
"""
 Precio (money) aumenta con el año (year): autos más nuevos valen más.

 Precio disminuye levemente con los kilómetros (kilometres): los autos usados valen un poco menos, pero la relación no es muy fuerte (probablemente porque hay otras variables que influyen más).

 La variable door no tiene impacto relevante en precio, año ni kilómetros.

 Kilometraje y año tienen una fuerte relación inversa: como es esperable (autos nuevos recorrieron menos kilómetros)."""