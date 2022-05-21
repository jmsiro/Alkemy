import requests
import locale
import os
from datetime import datetime 
from testdb import upload_file

# Used to change from english to spanish to use the month name in spanish for the folder name
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

def download_dbs(nombre, url):
    # Request - Downloads the file
    r = requests.get(url, allow_redirects=True)
    
    # Constructs the folders names: "category/YYYY-month"
    db = nombre + "/" + datetime.now().strftime("%Y") + "-" + datetime.now().strftime("%B")
    
    # Checks if it already exist, if not, creates it
    existe = os.path.exists(db)
    if not existe:
        os.makedirs(db)
    
    # Constructs the file name "category-dd-mm-yyyy" (Date when downloaded)
    file_name = nombre + "-" + datetime.now().strftime("%d-%m-%Y") + ".csv"
    
    full_path = db + "/" + file_name
    
    # Open the file and overwrite the data, if not exist, creates it
    open(full_path, 'wb').write(r.content)

    return full_path

museos_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
salas_cine_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
bibliotecas_url ='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

urls = {'museos': museos_url, 'salas_cine':salas_cine_url, 'bibliotecas':bibliotecas_url}

for key, value in urls.items():
    file_path = download_dbs (key, value)
    upload_file(file_path, key)