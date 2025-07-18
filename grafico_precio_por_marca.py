import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el CSV
datos = pd.read_csv("argentina_cars_normalizado.csv")

# Filtrar autos en dólares en un rango razonable
datos_dolares = datos[
    (datos['currency'] == 'dólares') &
    (datos['money'].between(5000, 150000))
]

# Filtrar autos en pesos en un rango razonable (ajustar valores según tus datos)
datos_pesos = datos[
    (datos['currency'] == 'pesos') &
    (datos['money'].between(1000000, 15000000))
]

# === Gráfico en DÓLARES ===
plt.figure(figsize=(12, 6))
sns.boxplot(x='brand', y='money', data=datos_dolares)
plt.xticks(rotation=90)
plt.title('Precio en Dólares por Marca (Filtrado)')
plt.ylabel('Precio en USD')
plt.xlabel('Marca')
plt.tight_layout()
plt.show()

# === Gráfico en PESOS ===
plt.figure(figsize=(12, 6))
sns.boxplot(x='brand', y='money', data=datos_pesos)
plt.xticks(rotation=90)
plt.title('Precio en Pesos por Marca (Filtrado)')
plt.ylabel('Precio en ARS')
plt.xlabel('Marca')
plt.tight_layout()
plt.show()

