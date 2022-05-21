# import psycopg2


# conexion1 = psycopg2.connect(database="postgres", user="root", password="root", host="127.0.0.1")
# cursor1=conexion1.cursor()
# sql="insert into articulos(descripcion, precio) values (%s,%s)"

# datos=("naranjas", 23.50)
# cursor1.execute(sql, datos)
# datos=("peras", 34)
# cursor1.execute(sql, datos)
# datos=("bananas", 25)
# cursor1.execute(sql, datos)

# conexion1.commit()
# conexion1.close()

import pandas
from sqlalchemy import create_engine
#dialect+driver://username:password@host:port/database

def upload_file(path, table_name):
    engine=create_engine("postgresql+psycopg2://root:root@localhost:5432/postgres")

    data_file = pandas.read_csv(path)
    try:
        data_file.to_sql(table_name, engine, if_exists= 'replace', index= False)

    except:
        print("Fallo la conexion...")

    finally:
        engine.dispose()