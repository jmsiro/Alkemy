import logging
import traceback
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)

def normalize_data(en, paths = list):
    """
    Normalizes data from the raw tables and creates a new table with the needed data.
    """
    dfs = []
    for file in paths:
        dfs.append(pd.read_csv(file))

    # Name of the columns that are needed
    needed_data = {'Cod_Loc':['cod_Loc', 'codigo_loc', 'código_loc', 'codigo_locación', 'código_locacion', 'código_locación','codigo_locacion',],
                'Id_Provincia':['id_provincia', 'idprovincia' , 'id_prov', 'idprov'],
                'Id_Departamento':['id_departamento', 'id_dep', 'id_dpto', 'iddepartamento', 'iddep', 'iddpto'],
                'Categoría':['categoría', 'categoria', 'categ', 'cat'],
                'Provincia':['provincia', 'provincias', 'prov'],
                'Localidad':['localidad', 'localidades', 'local'],
                'Nombre':['nombre', 'nom'],
                'Domicilio':['domicilio', 'dom', 'dirección', 'direccion'],
                'Código_postal':['código_postal', 'codigo_postal', 'cód_postal', 'cod_postal', 'cp'],
                'Código_de_Area': ['código_de_crea', 'codigo_de_area', 'código_area', 'codigo_area', 'códigoarea', 'codigoarea', 'cód_area', 'cod_area',
                                    'codarea','codarea', 'cod_tel', 'codtel'],
                'Número_de_teléfono':['número_de_teléfono', 'numero_de_teléfono', 'numero_de_telefono', 'teléfono','telefono', 'tel', 'num_tel', 'numtel'],
                'Mail':['mail', 'email', 'correo_electronico'],
                'Web':['web', 'pagina_web', 'paginaweb']}

    # Iterates through the Data Frames and through the Columns of each of them, then compares the columns titles with the nomalized values given in 'needed_data'. 
    # Finally replace the column titles with the corresponding key from 'needed_data'. 
    logging.info("Normalizing data...")
    for df in dfs:
        for col in df.columns:
            for k, v in needed_data.items():
                if col.lower() in v:
                    df.rename(columns={col:k}, inplace=True) # 'inplace=True' means that it does not return a copy, the renaming is done over the original data frame.
                else:
                    pass            

    # Creates a new data frame appending the ones given. The resulting dataframe only contains the columns that the 'input' data frames shares.
    data_file = pd.concat(dfs, join='inner', ignore_index=True,)

    # Eliminates the shared columns that are not needed for.
    for title in data_file.columns:
        if title in needed_data.keys():
            pass
        else:
            data_file.drop(labels=title, axis='columns', inplace=True)

    en = en.connect()
 
    try:
        data_file.to_sql('alkemydb', en, if_exists= 'replace', index= False)
        en.execute("""ALTER TABLE Alkemydb 
                   ADD fecha_de_carga date DEFAULT """ + "'" + datetime.now().strftime("%Y-%m-%d") + "'" + ";")
        logging.info("Table 'alkemydb' created/updated")
    except Exception as er:
        logging.error(traceback.format_exc(er))

        