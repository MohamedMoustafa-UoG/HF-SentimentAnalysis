from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, Pipeline
import threading

app = FastAPI()

# Use a lock to ensure thread safety
_pipeline = None
_pipeline_lock = threading.Lock()

def get_sentiment_pipeline() -> Pipeline:
    global _pipeline
    if _pipeline is None:
        with _pipeline_lock:
            if _pipeline is None:  # Double-check locking
                _pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return _pipeline

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Send a POST request to /predict with your text."}

@app.post("/predict")
def predict(input_data: TextInput):
    pipe = get_sentiment_pipeline()
    try:
        result = pipe(input_data.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))