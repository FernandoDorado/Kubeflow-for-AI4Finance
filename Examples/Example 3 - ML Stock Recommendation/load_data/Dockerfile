FROM python:3.8-slim
WORKDIR /pipeline

COPY data/ /pipeline/data/
COPY requirements.txt /pipeline
RUN pip install -r requirements.txt

COPY load_data.py /pipeline