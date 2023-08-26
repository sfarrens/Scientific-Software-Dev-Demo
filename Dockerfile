FROM continuumio/miniconda3

LABEL Description="MyCosmo Docker Image"
WORKDIR /home
ENV SHELL /bin/bash

RUN apt-get update
RUN apt-get install build-essential -y

COPY * .

RUN conda env create -f environment.yml