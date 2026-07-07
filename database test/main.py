import db_connector,export_tool
import pyodbc

cnxn = None

try:
    cnxn = db_connector.db_connect()

    if cnxn:
        export_tool.export_data(cnxn, 'csv') # Call the export_data function with the connection and desired output file type
        cnxn.close()

except Exception as e:
    print(f"An error occurred: {e}")