################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as ing

def signo(numero):
    if (numero == 0):
        print("El número es 0!")
        return 0
    if (numero > 0):
        print("El número es positivo!")
        return 1
    if (numero < 0):
        print("El número es negativo!")
        return -1

def prueba():
    num = ing.ingreso_entero("""Ingrese un número para determinar si es
    negativo, positivo o cero.""")
    print(signo(num))

if __name__ == "__main__":
    prueba() 