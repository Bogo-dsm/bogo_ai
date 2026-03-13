from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("SUMMARIZER_KEY")

from langchain.chat_models import init_chat_model
from schemas import json_schema

normal_model = init_chat_model("gpt-5-mini")
summarizer_model = normal_model.with_structured_output(json_schema)
