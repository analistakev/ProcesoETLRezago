#Python
import pathlib
import io

#Externas
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

#Propias
from settings.settings import *


#Función encargada de descargar archivos de DRIVE
def descargar(file_ids:list, file_names:list):
    creds = None
    creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

    service = build(API_NAME, API_VERSION, credentials=creds)

    for file_id, file_name in zip(file_ids, file_names):
        request = service.files().export_media(fileId=file_id, mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd = fh, request=request)
        done = False

        while not done:
            status, done = downloader.next_chunk()
            print("Download progress {0}".format(status.progress() * 100))

        fh.seek(0)

        with open(pathlib.Path(pathlib.Path(),'proceso-etl-rezago','datos',file_name).absolute(), "wb") as f:
            f.write(fh.read())
            f.close()


#Punto de entrada
if __name__ == '__main__':
    descargar(['1lZIBCHGWGQpG1gdZTE6nFRWis-wQ0vYtAY_dmbnPbOk'],['veracruz.xlsx'])