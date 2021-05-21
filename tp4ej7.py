################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def division_lenta(dividendo, divisor):
    cociente = 0
    decimal = False
    while (dividendo > 0):
        #print(dividendo)
        resto = dividendo
        dividendo = dividendo - divisor
        if (dividendo > 0):
            cociente = cociente + 1
        elif (dividendo == 0):
            cociente = cociente + 1
            return print(f"el cociente es {cociente} y tiene resto 0")
        else:
            print("entré en el else")
            decimal = True
    if (decimal == True):
        print("entré al decimal")
        dividendo = resto * 10
        print(f"el dividendo es {dividendo}")
        while (dividendo > 0):
            resto = dividendo
            dividendo = dividendo - divisor
            print(f"el dividendo es ahora {dividendo}")
            if dividendo == 0:
                resto = 0
            cociente = cociente + 0.1
            
                
            
    print(f"El cociente de la operación es: {cociente}")
    print(f"El resto de la operación es: {resto}")
        
        

def prueba():
    division_lenta(17,5)
    pass

if __name__ == "__main__":
    prueba() 