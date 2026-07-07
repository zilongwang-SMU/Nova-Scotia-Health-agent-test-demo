from langchain.tools import tool
import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv
 
@tool
def export_data(sql_query: str, output_file_name: str, output_file_type: str):
    """
    Exports all data from a specified database table to a local CSV or XLSX file.
    Use this tool when a user asks to export, save, or get data from a database table.
 
    Args:
        sql_query (str): The SQL query to execute.
        output_file_name (str): The name of the output file.
        output_file_type (str): The desired output format, must be either 'csv' or 'xlsx'.
    """

    # configure database connection parameters
    load_dotenv()
    DRIVER = os.environ.get('DB_DRIVER')
    SERVER = os.environ.get('DB_SERVER') 
    DATABASE = os.environ.get('DB_DATABASE') 
    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'
    cnxn = None

    # Establish a connection to the database
    try:
        cnxn = pyodbc.connect(conn_str)
        print("Database connection established.")
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Connection failed. Database Error Occurred: {sqlstate}")
        print(ex)
        return f"Error: Could not connect to the database. {ex}"
    
    try:
        df = pd.read_sql_query(sql_query, cnxn)
        if output_file_type.lower() == 'csv':
            df.to_csv(output_file_name, index=False)
        elif output_file_type.lower() == 'xlsx':
            df.to_excel(output_file_name, index=False)
        else:
            return f"Error: Unsupported file type '{output_file_type}'."
        return f"Success! {len(df)} rows exported to {output_file_name}.{output_file_type}"
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        if cnxn:
            cnxn.close()
            print("--- Tool finished: Database connection closed. ---")