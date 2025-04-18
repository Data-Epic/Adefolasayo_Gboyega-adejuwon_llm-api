import os
from groq import Groq
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='assistant.log')
logging.info("Starting Fast Food Support Assistant")


load_dotenv()


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Welcome to the Fast Food Support Assistant!")
print("Type 'EXIT' to end the conversation.")

while True:
    user_query = input("You: ")
    if not user_query.strip():
        print("Please enter a valid question.")
        logging.info("User provided empty input.")
        continue
    # Check if the user wants to exit
    if user_query.upper() == "EXIT":
        print("Thank you for using the Fast Food Support Assistant! Goodbye!")
        logging.info("User ended the conversation.")
        break
    messages = [
        {
            "role": "system",
            "content": "You are a helpful and friendly customer support assistant for a fast food restaurant. Your goal is to answer customer questions accurately and efficiently. Be concise and professional, but also approachable. When appropriate, mention menu items, promotions, store hours, and ordering processes relevant to a fast food context."
        },
        {
            "role": "user",
            "content": user_query,
        }
    ]
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )
        response = chat_completion.choices[0].message.content
        print("Assistant:", response)
        logging.info(f"Assistant response: {response}")
    except Exception as e:
        print("Error:", e)
        logging.error(f"Error during Groq API call: {e}")
        print("Please try again or type 'EXIT' to end.")
         


