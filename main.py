import os, sys
import init, message
from langchain.messages import AIMessage
def main():
    model = init.model_init()
    conversation_history = [message.system_msg]
    print("Data Agent is ready.")
    while True:
        response = ""
        huamn_message = message.read_input()
        conversation_history.append(huamn_message)
        for chunk in model.stream(conversation_history):
            if chunk.content:
                sys.stdout.write(chunk.content)
                sys.stdout.flush()
                response += chunk.content
        ai_msg = AIMessage(content=response)      
        conversation_history.append(ai_msg)
        print("\n")
if __name__ == "__main__":
    main()