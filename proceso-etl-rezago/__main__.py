#Python
import warnings
import pathlib
import sys

#Externas
import openpyxl 

#Propias
import functions.conectdrive as drive
import functions.connectdb as db
import functions.creacionreporte as cr
from settings.settings import *

#Función que encuentra las ordenes rezagadas

COLOR_ROSA = 'FFFF00FF'
COLOR_VERDE = 'FF00FF00'
COLOR_BLANCO = '00000000'
COLOR_AMARILLO = 'FFFFFF00'


def identificacion_ov(celdas_color,celdas_valor):

    #Declaración de los elementos
    element = 0
    celdas_rezagadas = []
    dias_rezago = []
    for i,celda in enumerate(celdas_color):
        element += 1
        try:
            if (celda.fill.fgColor.rgb == COLOR_ROSA) or \
                ((celda.fill.fgColor.rgb == COLOR_VERDE or celda.fill.fgColor.rgb == COLOR_BLANCO or celda.fill.fgColor.rgb == COLOR_AMARILLO) \
                 and (int(celdas_valor[i].value) >= 10)):
                celdas_rezagadas.append(element)
                dias_rezago.append(int(celdas_valor[i].value))
        except:
            pass
    return celdas_rezagadas,dias_rezago


#Script principal
def run():

    #Desactivacion de precauciones
    warnings.filterwarnings("ignore")
    
    #Hoja a analizar
    try:
        nombre_hoja = sys.argv[1]
    except:
        nombre_hoja = 'OCTUBRE 2023'
    
    #Descarga del archivo
    drive.descargar(ID_ARCHIVOS,NOMBRES_ARCHIVOS)

    #Rutas para leer los archivos
    ov_rezagadas = []
    dias_rezago = []

    db.reinicio_rezagos()

    for archivo in NOMBRES_ARCHIVOS:
        
        print("\033[1;33m"+f"\nAlmacen: {archivo}"+'\033[0;m')

        #Lectura tabla archivo
        ruta = pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos',archivo)
        excel = openpyxl.load_workbook(ruta, data_only=True)
        
        #Identificación de ordenes rezadas
        lineas,dias_rezago = identificacion_ov(excel[nombre_hoja]['B'], excel[nombre_hoja]['A'])

        #Guardado de las ordenes de venta rezagadas
        for i,linea in enumerate(lineas):
            ov_rezagadas.append(excel[nombre_hoja]['F'][linea-1].value.strip())
            print(f"Linea: {linea} | Orden de venta: {excel[nombre_hoja]['F'][linea-1].value} | Días de rezago: {dias_rezago[i]}")

        print(f"\nLíneas con rezagos: {lineas}")
        # print(f"\nov_rezagadas: {ov_rezagadas}")
        # print(f'\nSe han encontrado ov rezagadas en las lineas {lineas}')

        db.update_venta(ov_rezagadas, dias_rezago)

        lineas = []
        dias_rezago = []
        ov_rezagadas = []
    
    cr.create_excel()
    
    print("\nProceso terminado, rezagos actualizados.")


#Punto de entrada
if __name__ == '__main__':
    run()