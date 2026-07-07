import pyodbc
import os
from dotenv import load_dotenv

def db_connect():
    load_dotenv()
    server = os.environ.get('DB_SERVER')  
    database = os.environ.get('DB_DATABASE')
    username = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    driver= os.environ.get('DB_DRIVER')
    print(server)


    # --- Connection String ---
    #connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=WZ-20250327FJRL;'
        r'DATABASE=zilong;'
        r'Trusted_Connection=yes;'
    )

    try:
        # 1. Connect to the database
        print("Connecting to the database...")
        cnxn = pyodbc.connect(conn_str)
        print("Connection successful!")
        return cnxn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Connection failed. Database Error Occurred: {sqlstate}")
        print(ex)
        return None


