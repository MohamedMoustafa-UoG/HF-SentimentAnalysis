# Hugging Face Sentiment Analysis Demo

A FastAPI app serving a Hugging Face sentiment analysis model, Dockerized for Spaces.

## Usage

POST `/predict` with JSON:

```
{"text": "I love this API!"}
```

Returns:

```
{"result": [{"label": "POSITIVE", "score": 0.9998}]}
```