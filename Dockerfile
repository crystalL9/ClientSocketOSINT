FROM python:3.9

WORKDIR /app/src
COPY .env /app/src/
COPY . /app/src/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
