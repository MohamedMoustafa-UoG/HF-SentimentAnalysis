---

title: Sentiment Analysis API
emoji: 🧠
colorFrom: indigo
colorTo: blue
sdk: gradio
app_file: gradio_app.py
pinned: false
license: cc0-1.0
short_description: AI sentiment analysis using Gradio and social-tuned model
---

# Sentiment Analysis API 🧠

A simple and efficient AI-powered sentiment analysis tool that predicts the sentiment (positive, negative, or neutral) of a given text using the state-of-the-art `cardiffnlp/twitter-roberta-base-sentiment-latest` Hugging Face Transformers model. Delivered via an interactive web interface with Gradio and Docker.

## 🚀 Features

- **Modern Sentiment Model**: Uses `cardiffnlp/twitter-roberta-base-sentiment-latest` for robust results on social, real-world, and informal text
- **Interactive Web UI**: Built with Gradio—no code or REST calls needed, just use your browser
- **Fast & Lightweight**: Optimized Docker deployment for instant response
- **Flexible Input**: Works with social media, chat, feedback, and general-purpose text

## 🛠️ How It Works

1. **Input**: Type or paste your text into the web interface
2. **Process**: The model analyzes and predicts the sentiment (positive, neutral, negative)
3. **Output**: The UI displays the result and confidence score

## 📦 Web App Usage

- Visit the deployed Space (see Hugging Face link)
- Enter your text and press submit to see the sentiment

## 📊 Model Information

- **Model:** cardiffnlp/twitter-roberta-base-sentiment-latest
- **Task:** Sentiment classification (positive, neutral, negative)
- **Framework:** Hugging Face Transformers + PyTorch
- **Tuned for:** Real-world, social, and varied text input (not just reviews)

## 💡 Usage Tips

- Handles tweets, chat, reviews, informal, and general English
- Works well for short sentences and social language
- Not designed for deep clinical or medical language—see project notes

## 🔧 Technical Stack

- **Model:** Hugging Face Transformers (CardiffNLP Roberta)
- **Interface:** Gradio
- **Container:** Docker
- **Deployment:** Hugging Face Spaces

## 📈 Performance

- **Speed:** Fast inference (<1 second per request)
- **Quality:** Improved accuracy for diverse, real-world language

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
4. Open [http://localhost:7860/](http://localhost:7860/) in your browser to use the Gradio UI

## 🚦 CI/CD

- GitHub Actions build, test, and deploy the app to Hugging Face Spaces after each push to `main`.

## 📁 Project Structure

```
├── app.py              # FastAPI application (for optional REST API)
├── gradio_app.py       # Gradio web app (main entry point)
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

*Built with ❤️ using Hugging Face Transformers, Gradio, and Docker*