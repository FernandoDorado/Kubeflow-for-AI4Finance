FROM python:3.8-slim

COPY data/ /pipeline/data/
COPY requirements.txt /pipeline

WORKDIR /pipeline
RUN pip install -r requirements.txt

COPY preprocess_data.py /pipeline