import logging
import traceback
import pandas
from datetime import datetime
from sqlalchemy import create_engine
#dialect+driver://username:password@host:port/database

def upload_file(path, table_name):
    
    logging.info("Creating connection with DB Server...")
    engine = create_engine("postgresql+psycopg2://root:root@127.0.0.1:5432/postgres")
    data_file = pandas.read_csv(path)
    
    try:
        data_file.to_sql(table_name, engine, if_exists= 'replace', index= False)
        engine.execute("ALTER TABLE " + table_name + "\n"
                   "ADD fecha_de_carga date DEFAULT " + "'" + datetime.now().strftime("%Y-%m-%d") + "'" + ";")
        
        logging.info("Table created/updated: %s", table_name)
    
    except Exception as er:
        logging.error(traceback.fomat_exc())
    
    finally:
        logging.info("Closing connection...")
        engine.dispose()