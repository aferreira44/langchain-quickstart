import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)

print(llm)