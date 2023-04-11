from dotenv import load_dotenv
import os

import openai
import requests

# Loads env variables from .env file
load_dotenv()

# Access the API key from the env variable
openai.api_key = os.getenv("OPENAI_KEY")


def generate_response(msgs):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages=msgs
    )
    return response['choices'][0]['message']['content']


def main():
    print("Welcome to the GPT-4 Chatbot! Type 'q' to exit.")
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:

        user_input = input("You: ")
        if user_input.lower() == "q":
            break

        messages.append({"role": "user", "content": user_input})
        response = generate_response(messages)
        print("GPT-4: " + response)
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
