import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from utils import load_embeddings, load_db
from crypto_tracker import get_crypto_prices

load_dotenv()

class RetrievalChat:

    def __init__(self, api_key) -> None:
        # Set the OpenAI API key
        os.environ["OPENAI_API_KEY"] = api_key

        # Initialize bot components
        embedding_function = load_embeddings()
        db = load_db(embedding_function)
        self.qa = RetrievalQA.from_llm(llm=ChatOpenAI(temperature=0.1), retriever=db.as_retriever(kwargs={"k": 7}), return_source_documents=True)

        # Initialize conversation history
        self.conversation_history = ""
        self.name = "Ella"  # Initialize the bot's name

    def answer_question(self, question: str):
        # Update conversation history
        self.conversation_history += f"User: {question}\n"

        # Get bot's response
        output = self.qa({"query": self.conversation_history})

        # Update conversation history with bot's response
        self.conversation_history += f"{self.name}: " + output["result"] + "\n"

        return output["result"]

    def welcome(self):
        print(f"{self.name}: Welcome! What are we exploring today?")

if __name__ == "__main__":
    import constants  
    api_key = constants.API_KEY 
    # Initialize the bot with the API key
    qa = RetrievalChat(api_key)

    # Display the initial welcome message
    qa.welcome()

    while True:
        query = input("User: ")  # Add "User" as an identifier
        if query.lower() == "exit":
            confirmation = input(f"{qa.name}: Are you sure you want to exit the chat? (y/n): ")
            if confirmation.lower() == "y":
                break
        elif query.lower() == "reset":
            qa.conversation_history = ""
            print(f"{qa.name}: Conversation reset.")
        elif query.lower() == "check crypto":
            # Call the cryptocurrency report logic
            crypto_report = get_crypto_prices()
            print(crypto_report)  
        elif query.lower() == "new contract":
            # Prompt the user to select the contract type
            print("Available contract types:")
            print("1. Smart Contract")
            print("0. Return to main menu")
            user_input = input("User: Please enter the number corresponding to the contract type: ")

            if user_input == "1":
                # Launch the smart contract template
                os.system("python smartcontract_build.py")
            elif user_input == "0":
            # Relaunch the chat.py and break the loop
                os.system("python chat.py")
                break
            else:
                print(f"{qa.name}: Invalid input. Please enter a valid number.")
            print()  # Add a blank line for separation

        else:
            response = qa.answer_question(query)
            print(f"{qa.name}: {response}")
            print()
