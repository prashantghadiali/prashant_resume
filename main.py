import textbase
from textbase.message import Message
from textbase import models
import os, openai
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "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"
# or from environment variable:

# models.OpenAI.api_key = os.getenv("")
# print("here",models.OpenAI.api_key)

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    if state is None:
        state = {}

        # Extract user's message from the last element of message_history
        user_message = message_history[-1].split(":")[1].strip()

        # Bot's response generation logic based on user_message
        if "hello" in user_message.lower():
            bot_response = "Hi there! How can I help you?"
        else:
            bot_response = "I'm not sure how to respond to that."

        # Bot's response generation logic based on user_message
        if "prashant" in user_message.lower():
            bot_response = "Yes, Prashant Trained me. Here is the link of his website: " + "https://prashantghadiali.com"

        elif "prashant react" in user_message.lower():
            bot_response = "Yes, Prashant Trained me. Here is the link of his website this website is also built on React Library: " + "https://prashantghadiali.com"

        elif "prashant node" in user_message.lower():
            bot_response = "Yes, Prashant Trained me. He has Knowledge of Node and MongoDB."+"you can visit his git repositorey : https://github.com/prashantghadiali/User_auth_with_mongoDB"+" Here is the link of his website this website is also built on React Library: " + "https://prashantghadiali.com"
        
        elif "prashant javascript" in user_message.lower():
            bot_response = "Yes, Prashant Trained me. He has Knowledge of Javascript."+"you can visit his git repositorey : https://github.com/prashantghadiali/Superhero_API_Pure_Javascript"+" Here is the link of his website this website is also built on React Library: " + "https://prashantghadiali.com"
        elif "prashant chatbot" in user_message.lower():
            bot_response = "Yes, Prashant Trained me. He has Knowledge of Chatbot."+"you can visit his git repositorey : https://github.com/prashantghadiali/AI_Jarvis_project"+" Here is the link of his website this website is also built on React Library: " + "https://prashantghadiali.com"
        

        # Update state if needed
        state["counter"] = state.get("counter", 0) + 1
        return


    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state