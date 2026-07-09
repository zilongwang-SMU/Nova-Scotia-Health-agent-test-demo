from langchain.tools import tool
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from database.database_connector import db_connector

def sql_toolkit(llm):
    """
    Creates a SQL toolkit for interacting with a database using LangChain.
    
    Args:
        llm: The language model to use for generating SQL queries.
    """
    engine = db_connector()
    db = SQLDatabase(engine=engine)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    sql_tool = toolkit.get_tools()
    return sql_tool