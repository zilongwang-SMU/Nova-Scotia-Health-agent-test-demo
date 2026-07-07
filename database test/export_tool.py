import pandas as pd   

def export_data(cnxn, output_file_type):
    """
    Export data from the database to a CSV file.

    Args:
        output_file_type (str): The type of the output file ('csv' or 'xlsx').
    """
    # --- SQL Query ---
    sql_query = """
    SELECT 
        *
    FROM 
        CUSTOMER;
    """
    # --- Export Data to CSV ---
    output_filename = "exported_data" # Specify the output filename  
    df = pd.read_sql_query(sql_query, cnxn)
    try:
        if output_file_type == 'csv':
            df.to_csv(output_filename, index=False)
        elif output_file_type == 'xlsx':
            df.to_excel(output_filename, index=False)
        print(f"Success! {len(df)} rows have been exported to {output_filename}")
    
    except Exception as e:
        print(f"Error occurred while exporting data: {e}")