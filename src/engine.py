from sqlalchemy import create_engine
import logging
from decouple import config

def eng_con():
    """This function creates a connection with the database."""
    logging.info("Creating connection with DB Server...")
    en = "postgresql+psycopg2://{}:{}@{}:{}/postgres".format(config('POSTGRES_USER'), config('POSTGRES_PASSWORD'), config('DATABASE_HOST'), config('POSTGRES_PORT'))
    return create_engine(en)
    
def eng_dis(en):
    """This function shotsdown a connection with the database."""
    logging.info("Closing connection...")
    return en.dispose()