import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

def model_init():
    # Set up API key
    load_dotenv()
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

    # Initialize a model
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")

    return model