from langchain.tools import tool
import pandas as pd
from database.database_connector import db_connector

 
@tool
def export_data(sql_query: str, output_file_name: str, output_file_type: str):
    """
    Exports data from a specified SQL query to a local CSV or XLSX file.
    Use this tool when a user asks to export, save, or get data from a database.
 
    Args:
        sql_query (str): The SQL query to execute.
        output_file_name (str): The name of the output file (without extension).
        output_file_type (str): The desired output format, must be either 'csv' or 'xlsx'.
    """
    try:
        # Part 1: Connect to the database
        engine = db_connector()
        
        # Part 2: Execute the SQL query and export the results
        output_full_name = f"{output_file_name}"
        # The 'with' statement ensures the connection is automatically closed
        with engine.connect() as connection:
            print("Database connection established.")
    
            df = pd.read_sql_query(sql_query, connection)
 
            if output_file_type.lower() == 'csv':
                df.to_csv(output_full_name, index=False)
            elif output_file_type.lower() == 'xlsx':
                # For Excel, ensure you have openpyxl installed: pip install openpyxl
                df.to_excel(output_full_name, index=False)
            else:
                return f"Error: Unsupported file type '{output_file_type}'. Use 'csv' or 'xlsx'."
        
        return f"Success! {len(df)} rows were exported to {output_full_name}"
 
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"