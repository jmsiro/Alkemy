from sqlalchemy import create_engine
import logging

def eng_con():
    """This function creates a connection with the database."""
    logging.info("Creating connection with DB Server...")
    return create_engine("postgresql+psycopg2://root:root@127.0.0.1:5432/postgres")
    
def eng_dis(en):
    """This function shotsdown a connection with the database."""
    logging.info("Closing connection...")
    return en.dispose()