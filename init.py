import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from agent_tools import export_tool

def agent_init():
    # Set up API key
    load_dotenv()
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    tools = [export_tool.export_data] 
    # Initialize a agent
    agent = create_agent(model=model, tools=tools)
    return agent