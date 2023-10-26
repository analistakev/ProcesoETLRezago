# Proceso ETL Rezagos

Este módulo permite extraer las ordenes de venta rezagadas de los planes de embarque de cada almacen. El proceso de esta tarea se describe a contnuación.

# Instalación del módulo

Para realizar la instalación es necesario clonar el repositorio dentro de una carpeta del ordenador, para ello ejecuta la siguiente linea desde una terminal con acceso a git.

```
git clone https://github.com/analistakev/ProcesoETLSolarEver.git
```

Una vez clonado, para instalar el módulo es necesario correr la siguiente línea de comando en la terminal iniciada en la carpeta que contiene al módulo.

```
pip install -e ./proceso-etl-rezago
```

# Comando para su funcionamiento

Con el módulo instalado se corre la siguiente linea en una terminal para extraer la información de los rezagos de los archivos requeridos.

```
py -m proceso-etl-rezago
```