FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /mbapi
WORKDIR /mbapi
COPY api /mbapi/
COPY config /mbapi/
COPY main.py /mbapi/
COPY requirements.txt /mbapi/

RUN pip install -r requirements.txt
