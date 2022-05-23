import psycopg2
import pandas
from datetime import datetime
from sqlalchemy import create_engine
#dialect+driver://username:password@host:port/database

def upload_file(path, table_name):
    
    engine = create_engine("postgresql+psycopg2://root:root@127.0.0.1:5432/postgres")
    data_file = pandas.read_csv(path)
    
    # try:
    data_file.to_sql(table_name, engine, if_exists= 'replace', index= False)
    engine.execute("ALTER TABLE " + table_name + "\n"
                   "ADD fecha_de_carga date DEFAULT " + "'" + datetime.now().strftime("%Y-%m-%d") + "'" + ";")
        
        # conn = psycopg2.connect(user = 'root', 
        #                 password = 'root',
        #                 host = '127.0.0.1',
        #                 port='5432',
        #                 database = 'postgres')
        # cursor = conn.cursor()
        # cursor.execute()
        # cursor.close()   
    # except:
    #     print("Fallo la conexion...")
    # finally:
    engine.dispose()