import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el CSV
datos = pd.read_csv("argentina_cars.csv")

# Verificar los datos
print(datos.head())


#Relación precio vs kilometraje
plt.figure(figsize=(8,5))
sns.scatterplot(x='kilometres', y='money', data=datos)
plt.title('Relación precio vs kilometraje')
plt.xlabel('Kilometraje')
plt.ylabel('Precio')
plt.show()

"""" Conclusión visual:
Relación negativa: A más kilómetros → menor precio.

Alta dispersión: El precio no depende solo del kilometraje, hay otras variables que afectan (marca, año, tipo de auto, estado general).

Necesidad de limpiar o validar los datos con precios 0."""