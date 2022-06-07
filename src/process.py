import pandas as pd
import engine
import logging
from datetime import datetime

def reg_q():
    
    log_name = f"process_{datetime.now().strftime('%Y-%m-%d')}.log"

    logging.basicConfig(filename=log_name, level = logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    
    en = engine.eng_con()
    
    results = en.execute("""
                SELECT "Categoría", COUNT("Cod_Loc")
                FROM alkemydb
                GROUP BY "Categoría";
               """)
    
    df = pd.DataFrame(results)    
    logging.info(df)
    
    results1 = en.execute("""
                SELECT COUNT(*)
                FROM museos
                UNION
                SELECT COUNT(*)
                FROM bibliotecas
                UNION
                SELECT COUNT(*)
                FROM salas_cine;
               """)

    df1 = pd.DataFrame(results1)    
    logging.info(df1)

    results2 = en.execute("""
                SELECT "Categoría", "Provincia", COUNT("Cod_Loc")
                FROM alkemydb
                GROUP BY "Categoría", "Provincia"
                ORDER BY "Categoría", "Provincia";
               """)
    
    df2 = pd.DataFrame(results2)    
    logging.info(df2)

reg_q()

