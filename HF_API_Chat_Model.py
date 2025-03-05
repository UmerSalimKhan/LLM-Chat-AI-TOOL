import os # To deal with env var.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint # Using ChatHuggingFace for model creation and HuggingFaceEndpoint for model configuration and connection
from dotenv import load_dotenv # Dealing with dotenv file

# Load content from dotenv file
load_dotenv() 

# Retrieving the token from .env
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Model connection and configuration
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# Model instance
model = ChatHuggingFace(llm=llm, huggingfacehub_api_token=api_token, max_new_tokens=100) # Passing model configuration and loaded token 

# Model output 
# result = model.invoke("What is the capital of India?")
# print(result.content)

while True:
    user_input = input("User: ")
    user_input = user_input.lower()

    if user_input == "q" or user_input == "quit" or user_input == "exit":
        break

    result = model.invoke(user_input)
    ai_ans = result.content

    print(f"AI: {ai_ans}\n")