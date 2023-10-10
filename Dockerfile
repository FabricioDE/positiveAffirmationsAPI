FROM python:3.11


WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt







EXPOSE 8000-8010


CMD ["python", "main.py"]

