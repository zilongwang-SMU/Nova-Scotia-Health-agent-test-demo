import os, sys
import init, message
from langchain.messages import AIMessage
def main():
    # Initialize the model once
    model = init.model_init()
    # Initialize the conversation history with ONLY the system message
    conversation_history = [message.system_msg]
    print("Data Agent is ready.")

    while True:
        # Initialize an empty string for the AI response
        response = ""
        # Get a single HumanMessage object from the user
        huamn_message = message.read_input()
        conversation_history.append(huamn_message)

        # Stream AI's response using the full, correct conversation history
        for chunk in model.stream(conversation_history):
            if chunk.content:
                sys.stdout.write(chunk.content)
                sys.stdout.flush()
                response += chunk.content
                
        ai_msg = AIMessage(content=response)  
        # Append the AIMessage to the history    
        conversation_history.append(ai_msg)
        print("\n")

if __name__ == "__main__":
    main()
