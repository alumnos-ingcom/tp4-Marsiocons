################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def ordenar_mayor_a_menor(uno, dos, tres):

    if(tres < uno > dos):
        
        if(dos > tres):
            tupla = uno, dos, tres
        if(dos < tres):
            tupla = uno, tres, dos
            
    if(tres < dos > uno):
        
        if(uno > tres):
            tupla = dos, uno, tres
        if(uno < tres):
            tupla = dos, tres, uno
            
    if(uno < tres > dos):
        
        if(uno > dos):
            tupla = tres, uno, do
        if(uno < dos):
            tupla = tres, dos, uno
            
    return tupla

#def ordenar_menor_a_mayor(uno, dos, tres):

def prueba():
    num1 = ing.ingreso_entero("Ingrese el primer número:")
    num2 = ing.ingreso_entero("Ingrese el primer número:")
    num3 = ing.ingreso_entero("Ingrese el primer número:")
    print(ordenar_mayor_a_menor(num1,num2,num3))
    pass

if __name__ == "__main__":
    prueba() 