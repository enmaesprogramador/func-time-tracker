import time # Se importa la libreria time

def Medidor(func): # Se crea la funcion decoradora
    def medidor_de_tiempo(*args, **kwargs):# Funcion interna
        tiempo_inicial = time.time()# Variable tiempo inicial. Con la funcion time()
        result = func(*args, **kwargs) # Variable result. Es igual a la funcion y sus argumentos
        tiempo_final = time.time() # Tiempo de finalizacion de la funcion.  Con la funcion time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial # Variable de tiempo de ejecucion. Esta es igual a el tiempo final mas el tiempo inicial
        print(f'La funcion {func.__name__} a durado {tiempo_ejecucion: .6f} segundos en ejecutarse')# Print que imprime en nombre de la funcion mas el resultado de tiempo
        return result # Se retorna la variable resultado
    return medidor_de_tiempo # Se retorna la funcion interna


@Medidor
def funcion_lenta():
    time.sleep(2) # Funcion sleep(). Hace que la funcion se tome 2 segundos en ejecutarse
    print('La funcion lenta a terminado')
    
@Medidor
def funcion_rapido():
    print('La funcion rapida a terminado')
    
funcion_lenta()
funcion_rapido()