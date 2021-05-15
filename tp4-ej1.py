def funcion_uno(dato, intentos):
    while intentos > 0:
        if intentos <= 0:
            break
        try:
            dato_int = int(dato)
            if ( funcion_tres(dato_int) ):
                print(f"el número cumple con las características. ( {dato_int} )")
                break
            else:
                funcion_dos(dato, intentos)
                break
        except ValueError:
            print("no se puede transformar")
            funcion_dos(dato, intentos)
            return

def funcion_dos(dato, intentos):
    print(f"El dato es inválido: ( {dato} )")
    print(f"Intentos restantes: {intentos - 1}")
    intentos = intentos - 1
    if (intentos > 0):
        pedir_dato(intentos)

def funcion_tres(dato, dato_min=0, dato_max=10):
    if (dato >= dato_min and dato <= dato_max):
        return True
    else:
        return False

def pedir_dato(intentos=5):
    dato_new= input("Ingrese un dato: ")
    funcion_uno(dato_new, intentos)
    
    
pedir_dato()