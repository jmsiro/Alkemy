import logging
import traceback
import pandas
from datetime import datetime


#dialect+driver://username:password@host:port/database

def upload_file(path, table_name, en):
    """This function takes de data files and store them in the database."""
           
    en = en.connect()
    
    data_file = pandas.read_csv(path)
    
    try:
        data_file.to_sql(table_name, en, if_exists= 'replace', index= False)
        en.execute("ALTER TABLE " + table_name + "\n"
                   "ADD fecha_de_carga date DEFAULT " + "'" + datetime.now().strftime("%Y-%m-%d") + "'" + ";")
        logging.info("Table created/updated: %s", table_name)
    except Exception as er:
        logging.error(traceback.format_exc())
