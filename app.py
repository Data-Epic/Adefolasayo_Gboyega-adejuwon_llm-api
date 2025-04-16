import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Welcome to the Fast Food Support Assistant!")
print("Type 'EXIT' to end the conversation.")

while True:
    user_query = input("You: ")
    if user_query.upper() == "EXIT":
        print("Thank you for using the Fast Food Support Assistant! Goodbye!")
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
    except Exception as e:
        print("Error:", e)
        print("Please try again or type 'EXIT' to end.")
         








































































#template_folder='C:\\Users\\DELL\\Desktop\\Fola_python\\LLMS\\templates')