from files_down import download_dbs
from db_const import upload_file
from merge import normalize_data
import engine
from process import reg_cin, reg_conj
from datetime import datetime
from decouple import config
import time
import logging
import os

def main():    
    museos_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
    salas_cine_url = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
    bibliotecas_url ='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'

    urls = {'museos': museos_url, 'salas_cine':salas_cine_url, 'bibliotecas':bibliotecas_url}

    logging.info('Process started...')

    paths = []

    en = engine.eng_con()

    for key, value in urls.items():
        file_path = download_dbs (key, value)
        time.sleep(10)    
        upload_file(file_path, key, en)
        time.sleep(5)
        paths.append(file_path)
    time.sleep(5)
    normalize_data(en, paths)

    engine.eng_dis(en)
    logging.info('Process finished...')

    reg_conj()
    reg_cin()
    
if __name__ == '__main__':
    
    existe = os.path.exists(config('LOG_DIR'))
    if not existe:
        os.makedirs(config('LOG_DIR'))
    
    log_name = f"{config('LOG_DIR')}/alkemy_{datetime.now().strftime('%Y-%m-%d')}.log"
    logging.basicConfig(filename=log_name, level = logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    main()
    