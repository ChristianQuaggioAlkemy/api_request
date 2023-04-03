FROM python:3.10

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY requirements .
RUN pip install -r requirements
COPY . /app
ENV PYTHONPATH=/app

CMD [ "python3", "./api_request.py" ]
