FROM continuumio/miniconda3

LABEL Description="MyCosmo Docker Image"
WORKDIR /home
ENV SHELL /bin/bash

RUN apt-get update
RUN apt-get install -y build-essential && \
    apt-get install -y nano

COPY * .

RUN conda env create -f environment.yml

RUN echo "conda activate mycosmo" >> ~/.bashrc