import gradio as gr
from app import get_sentiment_pipeline

pipe = get_sentiment_pipeline()

def analyze_sentiment(text):
    result = pipe(text)
    label = result[0]["label"]
    score = result[0]["score"]
    return f"{label} ({score:.2f})"

demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=3, label="Input Text"),
    outputs=gr.Textbox(label="Sentiment"),
    title="Sentiment Analysis",
    description="Enter text to analyze sentiment using CardiffNLP Roberta."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)