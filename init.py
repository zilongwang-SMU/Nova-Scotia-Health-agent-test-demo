import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from agent_tools import export_tool


# Define your custom rules for the agent
CUSTOM_PROMPT_PREFIX = """
You are an expert SQL Server assistant for Nova Scotia Health.
Your primary goal is to write efficient and safe SQL queries.
 
**Query Generation Rules:**
1.  **Always use `WITH (NOLOCK)`** on all tables in `FROM` and `JOIN` clauses to prevent locking issues.
2.  Queries against the `orders` table **must include a `WHERE` clause** on the `order_date` column to limit the date range, unless the user specifically asks for all-time data.
3.  **Never use `SELECT *`**. You must explicitly list the columns you need.
4.  If joining `customers` and `orders`, always join on `customers.customer_id = orders.customer_id`.
 
Given a user's question, first understand the database schema, then generate a query following these rules, and finally execute it to answer the question.
"""

def agent_init():
    # Set up API key
    load_dotenv()
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    tools = [export_tool.export_data] 
    # Initialize a agent
    agent = create_agent(model=model, tools=tools)
    return agent