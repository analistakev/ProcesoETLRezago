#IMPORTANT:
#To install the package is necessary pre-install setuptools in your environment
#When you did the last, type: "pip install -e <directory-of-your-package>" in the terminal to finish the installation 
#It's necessary have the requirements.txt archive before the installation

from setuptools import setup, find_packages
import os

#requirements.txt lecture
REQUIREMENTS_PATH = os.path.join(os.path.curdir,'requirements.txt')
with open(REQUIREMENTS_PATH, 'r') as f:
    requires = f.readlines()
    for i in range(len(requires)):
        requires[i] = requires[i].replace('\n','')

#setup
setup(
   name='proceso_etl_rezagos',
   version='0.0.1',
   description='Este modulo contiene las funciones de la manipulación de archivos excel',
   author='KevCangas',
   author_email='kevin.guerrero@solarever.com.mx',
   packages= find_packages(),  # would be the same as name
   install_requires=requires #external packages acting as dependencies
)