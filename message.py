from langchain.messages import SystemMessage, HumanMessage

system_msg = SystemMessage("You are a helpful assistant that help user to clean"
     "and optimize datasets, including rename or add details in headers, remove duplicate entries,"
     "Handle Missing Data."
)

def read_input():
     user_input = input("User: ")
     human_msg = HumanMessage(content = user_input)
     return human_msg
    



