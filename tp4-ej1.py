################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(entrada):
    ingreso = input(f"{entrada} #")
    try:
        salida = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No se puede transformar") from err
    return salida


def prueba():
    print(ingreso_entero("Ingrese un número"))
    pass

if __name__ == "__main__":
    prueba()