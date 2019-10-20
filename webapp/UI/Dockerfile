FROM python:3.7-alpine

WORKDIR /app

ADD . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]