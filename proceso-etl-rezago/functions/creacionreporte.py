#Python
import pathlib
import csv

#Externas
import pandas as pd

#Propias
from settings.settings import *
from .connectdb import run_query


def create_excel():

    query = "SELECT * FROM ventassolarever.ordenesrezagadas"
    data = run_query(query)

    with open(pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos','reporte.csv').absolute(),'w') as f:
        c = csv.writer(f)
        for x in data:
            c.writerow(x)

    report = pd.read_csv(pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos','reporte.csv').absolute(),header=None,encoding='latin-1')
    report.columns = ['Almacen','Orden Venta','Factura','Vendedor','Producto','Unidades','Cliente','Fecha Facturacion','Dias Rezago']
    report.to_excel(pathlib.Path(pathlib.Path(),'proceso-etl-rezago','salida','reporte.xlsx').absolute(), index=False)

    print("\nReporte Generado")


    

