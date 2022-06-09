import pandas as pd
import engine
import logging
from datetime import datetime
import os
from openpyxl import Workbook
from decouple import config

def path():
    existe = os.path.exists(config('EXCELS_DIR'))
    if not existe:
        os.makedirs(config('EXCELS_DIR'))

def reg_conj():
    
    log_name = f"{config('LOG_DIR')}/process_conj_{datetime.now().strftime('%Y-%m-%d')}.log"
    logging.basicConfig(filename=log_name, level = logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    
    en = engine.eng_con()
    
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
    
    wb = Workbook()
    name = config('EXCELS_DIR') + "/pc_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
    ws =  wb.active
    ws.title = "Reg_tot_cat"
    wb.save(filename=name)

    with pd.ExcelWriter(name, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Reg_tot_cat")
        df1.to_excel(writer, sheet_name="Reg_tot_fuente")
        df2.to_excel(writer, sheet_name="Reg_prov_y_cat")

def reg_cin():
    
    log_name = f"{config('LOG_DIR')}/process_cin_{datetime.now().strftime('%Y-%m-%d')}.log"
    logging.basicConfig(filename=log_name, level = logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    
    en = engine.eng_con()
    
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
    
    wb = Workbook()
    name = config('EXCELS_DIR') + "/pc_" + datetime.now().strftime("%d-%m-%Y") + ".xlsx"
    ws =  wb.active
    ws.title = "Info_cines"
    wb.save(filename=name)

    with pd.ExcelWriter(name, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name="Info_cines")
