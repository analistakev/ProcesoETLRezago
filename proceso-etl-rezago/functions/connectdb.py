from settings.settings import *

import MySQLdb
import sys

from progress.bar import ChargingBar


#Function to realize a query
def run_query(query=''):
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    
    try:
        conn = MySQLdb.connect(*datos) # Conectar a la base de datos
    except:
        run_query(query)
        return
    
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 

    return data


#Actualización de rezago
def update_venta(ordenes:list,dias:list):

    #Carga de Articulos
    for i in range(len(ordenes)):
        
        #print(f"Query No. {i}: {ordenes[i]}")
        query = f"UPDATE ventassolarever.venta SET venta.culminado = 'N',venta.diasrezago = \'{dias[i]}\' WHERE venta.ordenventa = \'{ordenes[i]}\';" 
        run_query(query)
    
    try:
        print(f"Registros acutalizados: {i}")
    except:        
        print(f"Registros acutalizados: 0")
    
    #print("\nBase actualizada!")


def reinicio_rezagos():
    query = f"UPDATE ventassolarever.venta SET venta.culminado = 'S';" 
    run_query(query)