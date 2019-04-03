FROM python:3.6

RUN mkdir wordcount
COPY . /wordcount
WORKDIR /wordcount
RUN pip install -r requirements.txt
