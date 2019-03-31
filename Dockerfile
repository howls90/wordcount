FROM python:3.7

RUN mkdir wordcount
COPY . /wordcount
WORKDIR /wordcount
RUN pip install -r requirements.txt
