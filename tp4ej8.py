################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def ordenar_mayor_a_menor(uno, dos, tres):
    
    if(tres < uno > dos):
        if(dos > tres):
            tupla = (uno, dos, tres)
        if(dos < tres):
            tupla = (uno, tres, dos)
    if(tres < dos > uno):
        if(uno > tres):
            tupla = (dos, uno, tres)
        if(uno < tres):
            tupla = (dos, tres, uno)
    if(uno < tres > dos):
        if(uno > dos):
            tupla = (tres, uno, dos)
        if(uno < dos):
            tupla = (tres, dos, uno)
            
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    
    if(tres > uno < dos):
        if(dos < tres):
            tupla = (uno, dos, tres)
        if (dos > tres):
            tupla = (uno, tres, dos)
    if(tres > dos < uno):
        if(tres < uno):
            tupla = (dos, tres, uno)
        if(tres > uno):
            tupla = (dos, uno, tres)
    if(uno > tres < dos):
        if(uno > dos):
            tupla = (tres, dos, uno)
        if(uno < dos):
            tupla = (tres, uno, dos)
            
    return tupla

def prueba():
    num1 = ing.ingreso_entero("Ingrese el primer número:")
    num2 = ing.ingreso_entero("Ingrese el segundo número:")
    num3 = ing.ingreso_entero("Ingrese el tercer número:")
    print(ordenar_mayor_a_menor(num1,num2,num3))
    print(ordenar_menor_a_mayor(num1,num2,num3))

if __name__ == "__main__":
    prueba() 