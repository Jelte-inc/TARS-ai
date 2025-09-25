
from ai.ai_chat_model import ai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Voorbeeld input-model
class InputData(BaseModel):
    name: str
    number: int

# Root endpoint (GET)
@app.get("/")
def get(message: str):
    return ai(message)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=56277) 