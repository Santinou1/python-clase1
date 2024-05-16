"""
Crear un script de Python que permita al usuario sumar dos números enteros que él mismo ingrese.
Crea un nuevo archivo llamado sumadora.py.
Al inicio del script, imprime un mensaje de bienvenida al usuario. Por ejemplo: print("Bienvenido a la calculadora de sumas.")
Solicita al usuario que introduzca el primer número utilizando la función input(), y convierte este valor a entero. Puedes hacerlo de la siguiente manera: numero1 = int(input("Introduce el primer número: "))
Repite el paso anterior para obtener el segundo número.
Calcula la suma de ambos números y almacena el resultado en una variable: resultado = numero1 + numero2
Muestra el resultado al usuario: print("La suma de", numero1, "y", numero2, "es", resultado)

"""

print("Ejercicio de Sumar Numeros en Python")


# Solicitar un numero al usuario.

numero1= int(input("introduce el primer numero : "))

# Solicitar el Segundo numero al usuario

numero2= int(input("introduce el segundo numero : "))

# Suma Total

resultado= numero1+numero2

# Output al usuario

print("La suma de",numero1, "y",numero2,"es",resultado)