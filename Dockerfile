FROM python:3.10-alpine3.16

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY config.py .

COPY wsgi.py .

COPY api api

CMD ["python", "wsgi.py"]