import pandas as pd
from sqlalchemy import create_engine
import urllib
import os
from dotenv import load_dotenv

def db_connector():
 
    # Load environment variables
    load_dotenv()
    DRIVER = os.environ.get('DB_DRIVER')
    SERVER = os.environ.get('DB_SERVER') 
    DATABASE = os.environ.get('DB_DATABASE') 
        
    # URL-encode the driver to handle spaces and special characters
    quoted_driver = urllib.parse.quote_plus(DRIVER)
        
    # Create the standard SQLAlchemy connection URL
    connection_url = f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={quoted_driver}&Trusted_Connection=yes"
        
    # Create the engine, which manages connections
    engine = create_engine(connection_url)
        
    return engine
    
