FROM python:3.8-slim-buster

WORKDIR /python/app

# Copy the files for the server
COPY ./server /python/app

# Install pip packages
RUN pip install -r requirements.txt

# Server
CMD "uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload"