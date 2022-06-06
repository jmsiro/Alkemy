import pandas as pd
import engine

def reg_q():
    
    en = engine.eng_con()
    
    results = en.execute("""
                SELECT "Categoría", COUNT("Cod_Loc")
                FROM alkemydb
                GROUP BY "Categoría";
               """)
    
    df = pd.DataFrame(results)    
    print(df)
    
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
    print(df1)   

    results2 = en.execute("""
                SELECT "Categoría", "Provincia", COUNT("Cod_Loc")
                FROM alkemydb
                GROUP BY "Categoría", "Provincia"
                ORDER BY "Categoría", "Provincia";
               """)
    
    df2 = pd.DataFrame(results2)    
    print(df2)

reg_q()

