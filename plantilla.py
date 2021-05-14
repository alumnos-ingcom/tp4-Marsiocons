################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """El dato ingresado no es correcto."""
    pass 

def intentar_ingreso_numero(numIng):
    
    i = 0
    while (i < 5):
        NumIn = input("Ingrese un valor: ")
        try:
            int(NumIn)
            num = int(NumIn)
            print("Es un número!")
            if (type(num) == int):
                ingreso_entero_restringido(num)
                break
        except ValueError:
            print("Error: el dato ingresado no es un número!")
            print(f"Reintentar ({i+1} /5)")
            i = i + 1
    
#def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
#    print(mensaje)

def ingreso_entero_restringido(num, valor_minimo=0, valor_maximo=10):
    print(num)
    if not(num < valor_minimo and num > valor_maximo):
        print(f"El número tiene que ser mayor a {valor_minimo-1} y menor a {valor_maximo+1}")
def prueba():
    intentar_ingreso_numero(12)
    
if __name__ == "__main__":
    prueba()