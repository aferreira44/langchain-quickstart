import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
chat_model = ChatOpenAI()

print(llm.predict("Hi!"))
print(chat_model.predict("Hi!"))