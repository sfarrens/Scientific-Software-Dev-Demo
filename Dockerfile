FROM continuumio/miniconda3

LABEL Description="MyCosmo Docker Image"
WORKDIR /home
ENV SHELL /bin/bash

RUN apt-get update
RUN apt-get install -y build-essential && \
    apt-get install -y nano

# Copy the entire project structure
COPY . .

RUN conda env create -f environment.yml

# Use conda run to execute commands in the mycosmo environment
RUN conda run -n mycosmo python -m pip install .

RUN echo "conda activate mycosmo" >> ~/.bashrc