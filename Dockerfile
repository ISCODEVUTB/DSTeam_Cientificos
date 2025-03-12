FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY setup.py
COPY src/ src/
COPY tests/ tests/
COPY data/ data/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

RUN useradd -m appuser
USER appuser

CMD ["python", "-m", "src.core"] 
