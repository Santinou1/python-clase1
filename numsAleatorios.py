# Generar un conjunto de numeros aleatorios usando numpy
# Sacar promedios de esos numeros

import numpy as np

#Creacion de datos a analizar
numeros= np.random.randint(0,100,size=50)

#Analisis de datos
media= np.mean(numeros)
desviacion= np.std(numeros)

#Imprimir resultados

print("Numeros que se crearon para analizar ",numeros)
print("Media de los numeros ",media)
print("Desviacion de los numeros ",desviacion)

