FROM ubuntu:latest

MAINTAINER "antishipul@gmail.com"

ENV PATH /usr/local/bin:$PATH

RUN apt-get update                    \
    && apt-get install -y python3-pip \
    && cd /usr/local/bin              \
    && ln -s /usr/bin/python3 python

RUN apt-get update          \
    && apt-get install -y   \
    apt-utils bash vim curl \
    git gcc

COPY . project

RUN pip3 install --upgrade pip
RUN rm -rf $HOME/.cache/pip3/*
RUN pip3 install -r project/requirements.txt

RUN find project/ -name \*.pyc -delete

RUN pwd && ls -la

VOLUME ["./allure_/allure_results"]

WORKDIR project

CMD tail -f /dev/null
