FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src
