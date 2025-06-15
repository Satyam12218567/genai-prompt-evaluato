from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str
    response: str

@app.post("/evaluate/")
def evaluate(input: PromptInput):
    return {
        "prompt": input.prompt,
        "response": input.response,
        "evaluation": {
            "Instruction Following": "Yes",
            "Relevance": "Yes",
            "Tone": "Appropriate",
            "Hallucination": "No"
        }
    }
