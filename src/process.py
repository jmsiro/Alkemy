from dataclasses import replace
import pandas as pd
import engine
import logging
from datetime import datetime
import os
from openpyxl import Workbook

def reg_q():
    
    log_name = f"process_{datetime.now().strftime('%Y-%m-%d')}.log"
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

    wb = Workbook()
    name = "proccess_results" + "/" + datetime.now().strftime("%d-%m-%Y")
    wb.save(filename=name)

    with pd.ExcelWriter(name + ".xlsx", if_sheet_exists=replace) as writer:
        df.to_excel(writer, sheet_name="Registros totales por categoría")
        df1.to_excel(writer, sheet_name="Registros totales por fuente")
        df2.to_excel(writer, sheet_name="Registros por provincia y categoría")
reg_q()

