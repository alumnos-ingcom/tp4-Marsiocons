################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def es_primo(numero):
    divisores = 0
    
    if (numero < 0):
        numero = numero * -1
        
    for i in range(numero):
        if(numero % (i+1)  == 0):
            divisores = divisores + 1
    if (divisores > 2):
        return False
    else:
        return True

def prueba():
    num = ing.ingreso_entero("Ingrese un número para saber si es primo o no.")
    if(es_primo(num)):
        print("El número sí es primo!")
    else:
        print("El número no es primo!")
    pass

if __name__ == "__main__":
    prueba() 
