"""
Objetivo: Crear un script que simule la generación de una cantidad aleatoria de puntos de salud que un jugador puede recibir al usar una poción en un juego.

Importar la librería random: Asegúrate de importar la librería necesaria al inicio de tu script con import random.
Generar puntos de salud aleatorios: Utiliza random.randint() para generar un número aleatorio entre 1 y 100 que representará los puntos de salud que la poción otorgará.
Imprimir el resultado: Muestra en pantalla cuántos puntos de salud ha generado la poción, por ejemplo: "La poción te ha curado 45 puntos de salud."

"""

import random


print("Bienvenido a nuestro segundo ejercicio! ")

def generarVidaAleatoria():
    puntosDeSalud= random.randint(1,100)
    return puntosDeSalud

puntosHeleados= generarVidaAleatoria()

print("La pocion magia nos curo", puntosHeleados)