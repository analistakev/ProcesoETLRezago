#Python
import sys
import time
import warnings

#Externas
import openpyxl 

#Propias
import functions.conectdrive as drive
from settings import *


#Función que encuentra las ordenes rezagadas
def identificacion_ov(celdas):
    #Colores a identificar
    color_rosa = 'FFFF00FF'
    color_verde = 'FF00FF00'
    color_blanco = '00000000'

    #Declaración de los elementos
    element = 0
    result = []
    for celda in celdas:
        element += 1
        #print(celda.fill.fgColor.rgb)
        try:
            if celda.fill.fgColor.rgb == color_rosa:
                result.append(element)
            elif (celda.fill.fgColor.rgb == color_verde or celda.fill.fgColor.rgb == color_blanco) and (int(celda.value) >= 10):
                result.append(element)
        except:
            pass
    return result


#Script principal
def run():

    #Desactivacion de precauciones
    warnings.filterwarnings("ignore")
    
    #Lectura del mes a leer
    MES_LECTURA = sys.argv[1]

    #Descarga del archivo
    drive.descargar(ID_ARCHIVOS,NOMBRES_ARCHIVOS)

    #Rutas para leer los archivos
    ov_rezagadas = []
    for archivo in NOMBRES_ARCHIVOS:
        
        #Lectura tabla archivo
        ruta = "./datos/" + archivo
        tabla_excel = openpyxl.load_workbook(ruta, data_only=True)
        
        #Identificación de ordenes rezadas
        lineas = identificacion_ov(tabla_excel[MES_LECTURA]['A']) 
        
        #Guardado de las ordenes de venta rezagadas
        for linea in lineas:
            ov_rezagadas.append(tabla_excel[MES_LECTURA]['F'][linea-1].value)

        print(ov_rezagadas)
        print(f'Se han encontrado ov rezagadas en las lineas {lineas}')


#Punto de entrada
if __name__ == '__main__':
    run()