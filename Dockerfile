FROM python:3.9-slim

RUN pip install --no-cache-dir youtube-transcript-api openai

WORKDIR /app

COPY transcript.py /app/transcript.py

ENTRYPOINT ["python", "transcript.py"]

CMD []