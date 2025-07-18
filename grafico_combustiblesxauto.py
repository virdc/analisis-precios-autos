import pandas as pd
import matplotlib.pyplot as plt

# Leer CSV
datos = pd.read_csv("argentina_cars_normalizado.csv")

# Limpiar nombres de columnas
datos.columns = datos.columns.str.strip()

# Verificar nombres de columnas
print(datos.columns)

# Crear tabla cruzada
tabla = pd.crosstab(datos['brand'], datos['fuel_type'])

# Graficar apilado
tabla.plot(kind="bar", stacked=True, figsize=(12,6))

plt.title("Tipo de Combustible según Marca")
plt.xlabel("Marca")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)# Rota las etiquetas del eje X 45 grados.
plt.legend(title="Combustible")#Título
plt.tight_layout()#Ajusta automáticamente los márgenes del gráfico para que los títulos y etiquetas no queden recortados.
plt.show()
