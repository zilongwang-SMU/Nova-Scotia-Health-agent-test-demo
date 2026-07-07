import os, sys
import init, message
from langchain.messages import AIMessage
def main():
    # Initialize the agent once
    agent = init.agent_init()
    # Initialize the conversation history with ONLY the system message
    state = {"messages": [message.system_msg]}
    print("Data Agent is ready.")

    while True:
        # Initialize an empty string for the AI response
        response = ""
        # Get a single HumanMessage object from the user
        human = message.read_input()
        state["messages"].append(human)
        state = agent.invoke(state)
        print(state["messages"][-1].content)
        print("\n")

if __name__ == "__main__":
    main()
