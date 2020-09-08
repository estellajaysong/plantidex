RUN echo "slimbuster"
FROM python:3.8-slim-buster
RUN echo "set workdir"
WORKDIR /python/app

# Copy the files for the server
RUN echo "copy files"
COPY ./server /python/app
RUN echo "install packages"
# Install pip packages
RUN pip install -r requirements.txt
