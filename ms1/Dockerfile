
# Dockerfile for gateway application
FROM python:3.8-slim-buster

RUN apt-get update

RUN apt-get install -y netcat

RUN apt-get install -y vim

#RUN groupadd -g 999 appuser && \
#    useradd -r -u 999 -g appuser appuser

COPY requirements.txt /tmp
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY app /code/app
COPY api /code/api

#COPY config.yml /app/config.yml
COPY run.sh /code/run.sh
COPY manage.py /code/manage.py
COPY service.py /code/service.py
COPY rabbitmq_config.yml /code/rabbitmq_config.yml

RUN chmod +x /code/run.sh

#USER appuser
WORKDIR /code

CMD /code/run.sh

