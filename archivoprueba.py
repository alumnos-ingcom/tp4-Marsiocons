def funcion_uno(dato, intentos):
    while intentos > 0:
        try:
            dato_int = int(dato)
            print("pude transformar el número")
            if funcion_tres(dato_int):
                break
            elif ( funcion_dos(dato, intentos) > 0 ):
                intentos = intentos - 1
                pedir_dato(intentos)
                break
            else:
                print("Exceso de intentos")
                break
        except ValueError:
            print("no se puede transformar")
            if ( funcion_dos(dato, intentos) > 0 ):
                intentos = intentos - 1
                pedir_dato(intentos)
                break
            else:
                print("Exceso de intentos")
                break
            

def funcion_dos(dato, intentos=5):
    print(f"Vuelva a intentar. ( {dato} )")
    print(f"Intentos restantes: {intentos}")
    intentos = intentos - 1
    return intentos
    
def funcion_tres(dato, dato_min=0, dato_max=10):
    if (dato >= dato_min and dato <= dato_max):
        return True
    else:
        return False

def pedir_dato(intentos=5):
    dato_new= input("Ingrese un dato: ")
    funcion_uno(dato_new, intentos)
    
pedir_dato()