# syntax=docker/dockerfile:1
FROM python:3.8
EXPOSE 8501
WORKDIR /finohub
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD streamlit run app.py