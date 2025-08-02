---

## title: Sentiment Analysis API emoji: 🧠 colorFrom: indigo colorTo: blue sdk: docker app\_file: app.py pinned: false license: cc0-1.0 short\_description: AI-powered sentiment analysis using Hugging Face Transformers

# Sentiment Analysis API 🧠

A simple and efficient AI-powered sentiment analysis tool that predicts the sentiment (positive/negative) of a given text using a pre-trained Hugging Face Transformers model, delivered via a REST API with FastAPI and Docker.

## 🚀 Features

- **Accurate Sentiment Classification**: Uses `distilbert-base-uncased-finetuned-sst-2-english` for robust results
- **RESTful API**: Easily integrate sentiment analysis into any app or workflow
- **Fast & Lightweight**: Optimized Docker deployment for fast response
- **Developer Friendly**: OpenAPI docs available at `/docs`

## 🛠️ How It Works

1. **Input**: Send a POST request with your text to `/predict`
2. **Process**: The model analyzes the sentiment as positive or negative
3. **Output**: JSON response with label and confidence score

## 📦 API Usage

**POST** `/predict`

**Request:**

```json
{
  "text": "I love Hugging Face!"
}
```

**Response:**

```json
{
  "result": [
    { "label": "POSITIVE", "score": 0.9998 }
  ]
}
```

Try it interactively at [`/docs`](https://huggingface.co/spaces/MohamedMoustafa/hf-sentimentanalysis/docs).

## 📊 Model Information

- **Model:** distilbert-base-uncased-finetuned-sst-2-english
- **Task:** Sentiment classification (positive/negative)
- **Framework:** Hugging Face Transformers + PyTorch

## 💡 Usage Tips

- Works best with clear, single-sentence or short-paragraph input
- Use for reviews, social media, quick feedback tools, etc.

## 🔧 Technical Stack

- **Model:** Hugging Face Transformers (DistilBERT)
- **API:** FastAPI
- **Container:** Docker
- **Deployment:** Hugging Face Spaces

## 📈 Performance

- **Speed:** Fast inference for most short texts (<1 second per request)
- **Quality:** Good accuracy for modern English

## 💪 Local Development

1. Clone the repository.
2. Build the Docker image:
   ```bash
   docker build -t hf-sentimentanalysis .
   ```
3. Run the container:
   ```bash
   docker run -p 7860:7860 hf-sentimentanalysis
   ```
4. Test locally:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text":"I love Hugging Face!"}' http://localhost:7860/predict
   ```

## 🚦 CI/CD

- GitHub Actions build, test, and deploy the app to Hugging Face Spaces after each push to `main`.

## 📁 Project Structure

```
├── app.py              # FastAPI application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
├── app.yaml            # Hugging Face Docker config
├── .github/workflows/  # GitHub Actions workflows
│   └── ci.yml
├── README.md           # This file
```

## 🤝 Contributing

This project is open source! Feel free to:

- Report issues
- Suggest improvements
- Submit pull requests

**Repository**: [GitHub Link](https://github.com/MohamedMoustafa-UoG/HF-SentimentAnalysis)

## 📄 License

Creative Commons CC0 1.0 Universal (CC0 1.0) Public Domain Dedication – feel free to use, modify, or share for any purpose.

See [LICENSE](https://creativecommons.org/publicdomain/zero/1.0/) for details.

---

*Built with ❤️ using Hugging Face Transformers, FastAPI, and Docker*

