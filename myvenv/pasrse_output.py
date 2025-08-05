import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List


load_dotenv()

api_key=os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key is missing")

client = OpenAI()

class CalenderEvent(BaseModel):
    name:str
    date:str
    participants:List[str]




response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
        "role":"system",
        "content":"Extract the event information"
    },
    {
        "role":"user",
        "content":"Alice and Bob are going to a science fair on Friday."
    }
    ],
    text_format=CalenderEvent
)

event=response.output_parsed
print(event)