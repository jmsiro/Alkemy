import requests
import locale
import os
import logging
from datetime import datetime 

# Used to change from english to spanish to use the month name in spanish for the folder name
locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))

def download_dbs(nombre, url):
    """This funtion downloads the data files."""

    # Request - Downloads the file
    r = requests.get(url, allow_redirects=True)
    logging.info("Downloading from %s", url)
    
    # Constructs the folders names: "category/YYYY-month"
    db = "data"  + "/" + nombre + "/" + datetime.now().strftime("%Y") + "-" + datetime.now().strftime("%B")
    
    # Checks if it already exist, if not, creates it
    existe = os.path.exists(db)
    if not existe:
        os.makedirs(db)
    
    # Constructs the file name "category-dd-mm-yyyy" (Date when downloaded)
    file_name = nombre + "-" + datetime.now().strftime("%d-%m-%Y") + ".csv"
    
    full_path = db + "/" + file_name
 
    # Open the file and overwrite the data, if not exist, creates it
    open(full_path, 'wb').write(r.content)

    logging.info("File saved as: %s", full_path)
    
    return full_path