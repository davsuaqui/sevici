'''
Created on 25 nov. 2020

@author: David
'''
import csv
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from collections import namedtuple

# Creación de un tipo de namedtuple para las estaciones
Estacion = namedtuple('Estacion', 'nombre bornetas bornetas_vacias bicis_disponibles latitud longitud')

# Función de lectura que crea una lista de Estaciones
def lee_estaciones(fichero):
    ''' Lee el fichero de datos y devuelve una lista de estaciones
    
    ENTRADA: 
       - fichero: nombre del fichero CSV -> str
    SALIDA: 
       - lista de estaciones -> [Estacion(str, int, int, int, float, float)] 
    
    Cada estación se representa con una tupla con los siguientes valores:
    - Nombre de la estación
    - Número total de bornetas
    - Número de bornetas vacías
    - Número de bicicletas disponibles
    - Latitud
    - Longitud
    Usaremos el módulo csv de la librería estándar de Python para leer el
    fichero de entrada.
    Hay que saltar la línea de encabezado del fichero y comenzar a leer los datos
    a partir de la segunda línea.
    Hay que realizar un pequeño procesamiento con los datos numéricos. Hay que
    pasar del formato cadena (que es lo que se interpreta al leer el csv) a un
    valor numérico (para poder aplicar operaciones matemáticas si fuese necesario).
    '''
    
    registros= []
    with open(fichero, encoding= 'utf-8') as f:
        lector= csv.reader(f)
        next(lector)
        for nombre, bornetas, bornetas_vacias, bicis_disponibles, latitud, longitud in lector:
            
        
        
        
        
        
        