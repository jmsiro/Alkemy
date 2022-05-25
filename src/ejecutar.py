from datetime import datetime
from fileinput import filename
from files_down import download_dbs
from db_const import upload_file
from merge import normalize_data
from datetime import datetime
import time
import logging

museos_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
salas_cine_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
bibliotecas_url ='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

urls = {'museos': museos_url, 'salas_cine':salas_cine_url, 'bibliotecas':bibliotecas_url}

log_name = f"alkemy_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(filename=log_name, level = logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
logging.info('Process started...')

paths = []

for key, value in urls.items():
    file_path = download_dbs (key, value)
    time.sleep(10)    
    upload_file(file_path, key)
    time.sleep(5)
    paths.append(file_path)
time.sleep(5)
normalize_data(paths)
logging.info('Process finished...')
