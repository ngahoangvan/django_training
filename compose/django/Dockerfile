FROM python:3.9-alpine

RUN apk add build-base
ENV HOME /app/
WORKDIR $HOME
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Copy source
COPY . .
RUN python3 manage.py makemigrations && python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000

