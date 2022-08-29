FROM python:3.8-alpine

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP main.py
EXPOSE 5000
CMD flask run --host=0.0.0.0