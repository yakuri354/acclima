FROM eclipse-temurin:11

RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.11 python3.11-dev python3.11-venv python3-pip -y
RUN python3.11 -m pip install poetry

RUN mkdir /app
WORKDIR /app

COPY pyproject.toml poetry.lock .
RUN python3.11 -m poetry install
COPY . .

CMD ["python3.11", "-m", "poetry", "run", "uvicorn", "main:app"]