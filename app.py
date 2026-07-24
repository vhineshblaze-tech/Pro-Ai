import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

try:
    response = client.chat.completions.create(
        # 'openrouter/free' automatically picks whichever free model is online
        model="openrouter/free", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the rate of gold today?"}
        ],
        temperature=0.7,
        max_tokens=150
    )

    print("\n--- Response Output ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error: {e}")