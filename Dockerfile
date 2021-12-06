FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc postgresql-dev musl-dev python3-dev
RUN apk add libpq
RUN apk del --no-cache .build-deps

RUN mkdir -p /rockblock-proxy
COPY rockblock_proxy/ /rockblock-proxy/rockblock_proxy/
COPY requirements.txt /rockblock-proxy/requirements.txt
COPY setup.py /rockblock-proxy/setup.py
RUN pip install -e /rockblock-proxy

WORKDIR /rockblock-proxy

CMD uvicorn rockblock_proxy:app --host 0.0.0.0 --port 80
