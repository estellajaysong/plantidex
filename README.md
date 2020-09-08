# plantidex
An asynchronous plant image repository API.

## Motivation
I love plants. A while ago I started doing the [fast.ai Practical Deep Learning for Coders course](https://course.fast.ai/), and it's been at the top of my mind to try my hand at building a plant identification app ever since.

## Stack
- Python3
- Docker
- FastAPI
- MongoDB

## Features
- Dockerized 
- Easy setup (one command) with automated seeding if database is empty
- Asynchronous
- Strongly typed and validated with [Pydantic](https://pydantic-docs.helpmanual.io/)
- API reference generated from code (classes, typing, docstrings), which is a source of truth
- Search images by text, size, or another image (via image hashing)

## Start the server
```
# Start the server
docker-compose up

# Start the server in the background
docker-compose up -d

# See only app logs
docker-compose logs -f app
```

## API reference
API reference can be found at [http://localhost:8000/redoc](http://localhost:8000/redoc) once you start the server
