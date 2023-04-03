FROM python:3.10

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY requirements .
RUN pip install -r requirements
COPY . /app
ENV PYTHONPATH=/app

CMD [ "pytest", "-v" ]
