# Plantidex
An asynchronous plant image repository API. You can find it deployed at: [http://plantidex.herokuapp.com/images](http://plantidex.herokuapp.com/images/)

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
- Clean, interactive API reference generated from code (classes, typing, docstrings), which is a source of truth
- Search images by text, size, or another image (via image hashing)

## Future features
- Plant identification by image
- Plant idenfitication by characteristics
- CRUD operations on plants and images

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
API reference can be found at [http://plantidex.herokuapp.com/redoc](http://plantidex.herokuapp.com/redoc) or [http://localhost:8000/redoc](http://localhost:8000/redoc) once you start the server locally
