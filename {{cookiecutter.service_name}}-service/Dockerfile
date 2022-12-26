FROM python:3.11-slim

EXPOSE 8080

RUN apt-get --assume-yes update && apt-get --assume-yes install gcc musl-dev libffi-dev bash openrc nginx git

RUN mkdir /apps && mkdir /apps/deployment

COPY requirements.txt /apps/requirements.txt

RUN pip install -r /apps/requirements.txt

RUN mkdir /apps/app
COPY /app /apps/app/
COPY /deployment /apps/deployment/

RUN mkdir /apps/files && \
    mkdir /apps/settings && \
    mkdir /apps/settings/env && \
    mkdir /apps/settings/secrets && \
    mkdir /apps/settings/test

RUN chmod +x /apps/deployment/startup/app.sh && \
    chmod +x /apps/deployment/startup/locust.sh && \
    chmod +x /apps/deployment/startup/test.sh

WORKDIR /apps/app
