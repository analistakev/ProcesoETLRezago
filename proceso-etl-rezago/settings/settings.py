import pathlib

#GOOGLE API
KEY = pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos','key.json').absolute()
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

ID_ARCHIVOS = ['1lZIBCHGWGQpG1gdZTE6nFRWis-wQ0vYtAY_dmbnPbOk',
               '1lJ9xcaa5Y2uMrcoIUsV57v4msTgfeofc-s5MEcKY9zQ',
               '1KGEGOctDlfgfFUi_b7KFYGRCNDsXaqP1V-1FouF82ts',
               '1HIaGU8EqbJ3r_5fBxxxc3idtABUNdj-qhtWXFPC9vKo',
               '11QoV5qSNOAB-vF5yc0zYqsvXsLhySFdR5_BBqcLYUY4',
               '1WYqLk3cCVP7VNwqtx9eKtZzPjy8i5ly8nAEe3cyVAOo',
               '1SR3xaMVKgxiR4P0zd9eUddgKwa-zMGSXTZ0f370iFcM',
               '1DQEhDFcTzDnGmOsLBc8WNDYMBNOPg1ylNoLbuUsTfCg',
               '1Ob9aVrIg_IZLAKO2KjTX21aNwJOE14XDOGnwC9WEMAc']
               #'1gjLcFy2oO_WltbniNr0rbJ5uxVBzogHA']

NOMBRES_ARCHIVOS = ['Veracruz.xlsx','Leon.xlsx','Tijuana.xlsx',
                    'Monterrey.xlsx','Merida.xlsx','Guadalajara.xlsx',
                    'Cuautitlan.xlsx','Chihuahua.xlsx','Aguascalientes.xlsx']
                    #'Tecoman.xlsx']

#BASE DE DATOS
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'root' 
DB_NAME = 'ventassolarever' 