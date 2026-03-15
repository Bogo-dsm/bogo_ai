from .model import summarizer_model
from .prompts import summarize_prompt

def summarize(text:str) -> dict:
    response = summarizer_model.invoke(f'{summarize_prompt}{text}')
    return response