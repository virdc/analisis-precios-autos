import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el CSV
datos = pd.read_csv("argentina_cars_normalizado.csv")


#Cantidad de autos por tipo

# Cambia el tamaño de la figura
plt.figure(figsize=(8,5))

# Crea el gráfico de barras con Seaborn
sns.countplot(x='body_type', data=datos)

# Agrega un título
plt.title('Cantidad de autos por tipo de carrocería')

# Rota las etiquetas del eje X 45 grados (para que no se superpongan si son largas)
plt.xticks(rotation=45)

# Muestra el gráfico
plt.show()