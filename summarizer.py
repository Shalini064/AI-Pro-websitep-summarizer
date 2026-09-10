import os
from urllib import response
from openai import OpenAI
from dotenv import load_dotenv
from scraper import fetch_website_content

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

system_prompt = "You are a helpful assistant that summarizes website content."

def summarize_website(url):
    website = fetch_website_content(url)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Summarize the following website content:\n{website}"
            }
        ]
    )
    return response.choices[0].message.content




