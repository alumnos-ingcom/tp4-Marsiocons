################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_palindromo(texto):
    
    mitad_uno_texto = []
    mitad_dos_texto = []
    
    ### Si es par, le sacamos letra del medio a la palabra
    if ((len(texto) % 2) > 0):
        
        texto_par = []
        
        letra_medio = int(len(texto) / 2)
        
        for i in range(len(texto)):
            if(texto[i] != texto[letra_medio]):
                texto_par.append(texto[i])
        texto = texto_par
        
    ### Obtenemos la primera mitad de letras de la palabra    
    for i in range(int(len(texto)/2)):
        mitad_uno_texto.append(texto[i])
        
    ### Obtenemos la segunda mitad de letras de la palabra
    for i in range(int(len(texto)/2)):
        if i == 0:
            mitad_dos_texto.append(texto[i-1])
        else:
            mitad_dos_texto.append(texto[i*-1-1])
            
    ### Comparamos las mitades
    if (mitad_uno_texto == mitad_dos_texto):
        return True
    else:
        return False

def prueba():
    print(es_palindromo("asdfdsa"))

if __name__ == "__main__":
    prueba() 
