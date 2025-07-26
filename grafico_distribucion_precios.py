import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Leer el CSV
datos = pd.read_csv("argentina_cars_normalizado.csv")
#hacer por pesos
# Verificar los datos
print(datos.head())


import numpy as np

# Reemplazo limpio (solo una línea necesaria)
datos['money'] = datos['money'].replace(0, np.nan)

# Eliminar filas donde 'money' es NaN
datos.dropna(subset=['money'], inplace=True)

# Verificar resultados
print(datos['money'].isna().sum())  # Debería dar 0
print(datos.head())  # Ver los primeros registros



#Distribución de precios
plt.figure(figsize=(8,5))
sns.histplot(datos['money'], kde=True)
plt.title('Distribución de precios')
plt.xlabel('Precio')
plt.ylabel('Cantidad')
plt.show()





