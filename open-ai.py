from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a short poem about the beauty of nature."
        }
    ]
)

print(response.choices[0].message.content)
