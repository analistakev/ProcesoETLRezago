#Python
import sys
import time
import warnings
import pathlib

#Externas
import openpyxl 

#Propias
import functions.conectdrive as drive
import functions.connectdb as db
import functions.creacionreporte as cr
from settings.settings import *


#Función que encuentra las ordenes rezagadas
def identificacion_ov(celdas_color,celdas_valor):
    #Colores a identificar
    color_rosa = 'FFFF00FF'
    color_verde = 'FF00FF00'
    color_blanco = '00000000'

    #Declaración de los elementos
    element = 0
    celdas_rezagadas = []
    dias_rezago = []
    for i,celda in enumerate(celdas_color):
        element += 1
        #print(celda.fill.fgColor.rgb)
        try:
            if (celda.fill.fgColor.rgb == color_rosa) or \
                ((celda.fill.fgColor.rgb == color_verde or celda.fill.fgColor.rgb == color_blanco) and \
                 (int(celdas_valor[i].value) >= 10)):
                celdas_rezagadas.append(element)
                dias_rezago.append(int(celdas_valor[i].value))
        except:
            pass
    return celdas_rezagadas,dias_rezago


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
    dias_rezago = []

    db.reinicio_rezagos()

    for archivo in NOMBRES_ARCHIVOS:
        
        #Lectura tabla archivo
        ruta = pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos',archivo)
        tabla_excel = openpyxl.load_workbook(ruta, data_only=True)
        
        #Identificación de ordenes rezadas
        lineas,dias_rezago = identificacion_ov(tabla_excel[MES_LECTURA]['B'],tabla_excel[MES_LECTURA]['A'])

        #Guardado de las ordenes de venta rezagadas
        for linea in lineas:
            ov_rezagadas.append(tabla_excel[MES_LECTURA]['F'][linea-1].value)

        print(f"\nAlmacen: {archivo}")
        # print(f"\nov_rezagadas: {ov_rezagadas}")
        # print(f'\nSe han encontrado ov rezagadas en las lineas {lineas}')

        db.update_venta(ov_rezagadas,dias_rezago)

        lineas = []
        dias_rezago = []
        ov_rezagadas = []
    
    cr.create_excel()
    
    print("\nListo!")


#Punto de entrada
if __name__ == '__main__':
    run()