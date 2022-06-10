import pandas as pd
import engine
import logging
from datetime import datetime
import os
from openpyxl import Workbook
from decouple import config

logger = logging.getLogger(__name__)

def path():
    """
    Checks if the path exists or not. If not, it creates it.
    """
    existe = os.path.exists(config('EXCELS_DIR'))
    if not existe:
        os.makedirs(config('EXCELS_DIR'))

def reg_conj():
    """
    Creates an Excel file in which stores in three worksheets the resulting tables of the made queries to the joint DB.
    """
    en = engine.eng_con()
    
    logging.info("Making queries in joint table...")
    
    results = en.execute("""
                SELECT "Categoría", COUNT("Cod_Loc") AS "Cantidad por categoría"
                FROM alkemydb
                GROUP BY "Categoría";
               """)
    
    df = pd.DataFrame(results)
    
    results1 = en.execute("""
                SELECT
                    'Museos' as "Fuente",
                    COUNT(*) as "Cantidad de registros"
                FROM museos
                UNION
                SELECT
                    'Bibliotecas' as "Fuente",
                    COUNT(*) as "Cantidad de registros"
                FROM bibliotecas
                UNION
                SELECT
                    'Salas de Cine' as "Fuente",
                    COUNT(*) as "Cantidad de registros"
                FROM salas_cine;
               """)

    df1 = pd.DataFrame(results1)    

    results2 = en.execute("""
                SELECT "Categoría", "Provincia", COUNT("Cod_Loc") AS "Cantidad por Provincia"
                FROM alkemydb
                GROUP BY "Categoría", "Provincia"
                ORDER BY "Categoría", "Provincia";
               """)
    
    df2 = pd.DataFrame(results2)
    
    path()
    
    # Creates and save the Excel file.
    wb = Workbook()
    name = config('EXCELS_DIR') + "/joint_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
    ws =  wb.active
    ws.title = "Reg_tot_cat"
    wb.save(filename=name)

    # Writes the results of the query into the Excel created above.
    with pd.ExcelWriter(name, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Reg_tot_cat")
        df1.to_excel(writer, sheet_name="Reg_tot_fuente")
        df2.to_excel(writer, sheet_name="Reg_prov_y_cat")

    logging.info("File saved as: %s", name)
    
    engine.eng_dis(en)
    
def reg_cin():
    """
    Creates an Excel file in which stores the resulting table of the made querie to the cinemas DB.
    """
    en = engine.eng_con()
    
    logging.info("Making queries in cinemas database...")
        
    results = en.execute("""
                SELECT "Provincia", 
                SUM ("Pantallas") AS "Q_Pantallas", 
                SUM ("Butacas") AS "Q_Butacas", 
                COUNT("espacio_INCAA" LIKE 'si') AS "Q_INCAA"
                FROM salas_cine
                GROUP BY "Provincia";
               """)
    
    df = pd.DataFrame(results)
    
    path()
    
    # Creates and save the Excel file.
    wb = Workbook()
    name = config('EXCELS_DIR') + "/cinemas_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
    ws =  wb.active
    ws.title = "Info_cines"
    wb.save(filename=name)

    # Writes the results of the query into the Excel created above.
    with pd.ExcelWriter(name, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Info_cines")

    logging.info("File saved as: %s", name)
    
    engine.eng_dis(en)
    
reg_conj()
reg_cin()