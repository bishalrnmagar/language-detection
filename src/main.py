from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline

app = FastAPI()

class Text(BaseModel):
    text: str

class Prediction(BaseModel):
    text: str
    language: str

@app.get("/")
def home():
    return {
        "health_check": "OK", 
        "message": "Hello, World!"
    }

@app.post('/predict', response_model=Prediction)
def predict_language(request: Text):
    language = predict_pipeline(request.text)
    text = request.text
    return {
        'text': text, 
        'language': language
    }