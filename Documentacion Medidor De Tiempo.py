"""
Medidor de Tiempo Decorador

Este script implementa un decorador de funciones llamado 'Medidor' que calcula y muestra el tiempo de ejecución de una función. El decorador se utiliza para medir cuánto tiempo lleva ejecutar una función y se aplica a dos funciones de ejemplo: 'funcion_lenta' y 'funcion_rapido'.

Librerías utilizadas:
- time: Esta librería proporciona funciones para trabajar con el tiempo, como medir el tiempo de ejecución de las funciones.

Funciones definidas:
- Medidor(func): Una función decoradora que toma otra función 'func' como argumento y devuelve una función interna 'medidor_de_tiempo'. Esta última función interna mide el tiempo de ejecución de 'func' y muestra el resultado.

Funciones decoradas:
1. @Medidor
   def funcion_lenta():
       Esta función simula una operación lenta usando 'time.sleep(2)' y luego muestra un mensaje cuando termina.

2. @Medidor
   def funcion_rapido():
       Esta función muestra un mensaje cuando termina. No contiene operaciones que consuman mucho tiempo.

Uso:
Se aplican los decoradores '@Medidor' a las funciones 'funcion_lenta' y 'funcion_rapido'. Al llamar a estas funciones decoradas, se medirá el tiempo de ejecución y se mostrará un mensaje indicando la duración.

"""

import time  # Se importa la librería time

def Medidor(func):
    """
    Decorador para medir el tiempo de ejecución de una función.
    
    Parameters:
        func (function): La función a la que se le aplicará el decorador.
        
    Returns:
        function: Una función interna que calcula y muestra el tiempo de ejecución de 'func'.
    """
    def medidor_de_tiempo(*args, **kwargs):
        """
        Función interna que calcula y muestra el tiempo de ejecución de la función 'func'.
        
        Parameters:
            *args: Argumentos posicionales para 'func'.
            **kwargs: Argumentos de palabra clave para 'func'.
            
        Returns:
            Any: El resultado de la función 'func'.
        """
        tiempo_inicial = time.time()
        result = func(*args, **kwargs)
        tiempo_final = time.time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print(f'La función {func.__name__} ha durado {tiempo_ejecucion:.6f} segundos en ejecutarse')
        return result
    return medidor_de_tiempo

@Medidor
def funcion_lenta():
    """
    Función de ejemplo que simula una operación lenta.
    """
    time.sleep(2)
    print('La función lenta ha terminado')
    
@Medidor
def funcion_rapido():
    """
    Función de ejemplo que no consume mucho tiempo.
    """
    print('La función rápida ha terminado')
    
funcion_lenta()
funcion_rapido()