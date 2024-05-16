"""
Objetivo: Escribir un programa que solicite al usuario su dirección de correo electrónico y extraiga el nombre de usuario (parte antes de '@').

Solicitar el email al usuario: Usa la función input() para pedir al usuario que introduzca su dirección de email.
Extraer el nombre de usuario: Utiliza los operadores de cadena o métodos de string para separar el nombre de usuario del dominio.
Mostrar el resultado: Imprime el nombre de usuario extraído en la pantalla.

Puntos extra: investigar cómo se hace para validar que un string tiene forma de dirección de email correcta.
let reCorto = /\S+@\S+\.\S+/

"""

import re


def extraerUsuarioDelEmail(email):
    # Utilizamos una funcion regular para corrobora si el usuario envia un email valido, en caso que de true vamos a extraerle el usuario
    if re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",email):
        # Si el formato es valido vamos a extraer el nombre de usuario antes  del @ y el nombre del dominio despues del @
        usuario, dominio = email.split("@")
        return usuario , dominio
    else:
        return None
    

def pedirEmail():
    email= input("Por favor, introduzca tu direccion de correo electronico: ")
    usuario, dominio=extraerUsuarioDelEmail(email)
    if usuario and dominio: 
        print("El nombre de usuario es:", usuario)
        print("El nombre de dominio es:", dominio)
    else:
        print("La direccion de correo electronico no tiene un formato valido")



pedirEmail()