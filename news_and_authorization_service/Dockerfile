FROM python:3.11-slim

RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y libpq-dev gcc netcat-traditional

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x run_app.sh

ENTRYPOINT ["/app/run_app.sh"]
