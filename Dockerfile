FROM python:3.8

RUN pip install pipenv

WORKDIR /app

COPY ./Pipfile* /app/ 

RUN cd /app && \
    pipenv install --system --deploy
