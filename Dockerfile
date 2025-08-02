FROM python:3.10-slim

# Avoid pip cache, set up non-root user
RUN useradd -m appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER appuser

EXPOSE 7860
CMD ["python", "gradio_app.py"]