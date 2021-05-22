################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej9 as primo
import tp4ej1 as ing

def factores_primos(numero):
    lista= []
    go = True
    i = 2
    while go:
        if numero == 1:
            if (len(lista) > 0):
                factores_primos = tuple(lista)
                return factores_primos
            else:
                lista.append(int(numero))
                factores_primos = tuple(lista)
                return factores_primos
        if (primo.es_primo(i)):
            if(numero % (i) == 0):
                numero = numero / (i)
                lista.append(i)
            else:
                i = i + 1
        else:
            i = i + 1

def prueba():
    num = ing.ingreso_entero("Ingrese un número para buscar sus factores primos!")
    print(factores_primos(num))
    pass

if __name__ == "__main__":
    prueba() 
