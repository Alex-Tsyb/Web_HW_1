FROM ubuntu:20.04

RUN apt update && apt install -y python3-pip

RUN pip install pipenv

COPY app /app

COPY Pipfile /app
COPY Pipfile.lock /app
COPY requirements.txt /app

WORKDIR /app

ENTRYPOINT ["python3", "__main__.py"]
