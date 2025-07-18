import pandas as pd
# Leer el archivo CSV
datos = pd.read_csv("argentina_cars.csv")

# Mostrar las columnas disponibles
datos.columns.tolist()

# Ver cantidad de datos faltantes por columna
faltantes = datos.isnull().sum()

# Mostrar solo las columnas que tienen datos faltantes
print("Muestra los datos faltantes en cada columna:")
print(faltantes[faltantes > 0])

print("Muestra porcentaje de datos faltantes por columna:")
porcentaje_faltantes = (datos.isnull().sum() / len(datos)) * 100
print(porcentaje_faltantes[porcentaje_faltantes > 0])


# Mostrar las primeras 5 filas
print(datos.head(5))


# Ver las columnas y tipos de datos
print(datos.info())

# Estadísticas generales
print(datos.describe(include='all'))

# Marcas más frecuentes
print("Marcas más frecuentes:")
print(datos['brand'].value_counts())


# Configurar formato de salida
pd.options.display.float_format = '{:,.2f}'.format

# Calcular precio promedio por marca y currency
precio_promedio = datos.groupby(['brand', 'currency'])['money'].mean().reset_index()

# Ordenar por currency y money
precio_promedio = precio_promedio.sort_values(by=['currency', 'money'], ascending=[True, False])

# Mostrar resultado
print("Precio promedio por marca y tipo de moneda:")
print(precio_promedio)




# Mostrar resultados
print("Precio promedio por marca y tipo de moneda:")
print(precio_promedio)


# Filtrar autos en pesos
print("Autos en pesos:")
print(len(datos[datos['currency'] == 'pesos']))


# Filtrar autos en dólares
print("Autos en dólares:")
print(len(datos[datos['currency'] == 'dólares']))

# Autos usados con más de 50.000 km
print("Autos con más de 50.000 km:")
print(len(datos[datos['kilometres'] > 50000]))


# Conteo por tipo de combustible
print("Cantidad por tipo de combustible:")
print(datos['fuel_type'].value_counts())

#Autos mas nuevos y mas viejos
print("Año más nuevo:", datos['year'].max())
print("Año más viejo:", datos['year'].min())


#Relacion de típo de carrocería y cantidad de puertas 
print(datos.groupby('body_type')['door'].value_counts())

#Distribución de autos por color
print(datos['color'].value_counts())


#Autos que tienen el kilometraje = 0
print("Autos 0KM")
print(len(datos[datos['kilometres'] == 0]))

#Normalización y estandarización de datos
#Rellenar datos nulos(Desconocido)
datos['color'] = datos['color'].fillna('Desconocido')
datos['motor'] = datos['motor'].fillna('Desconocido')
print("Muestra los datos faltantes en cada columna:")
faltantes = datos.isnull().sum()
print(faltantes[faltantes > 0])




#Normalizar int float de las columnas
datos.to_csv("argentina_cars_normalizado.csv")


