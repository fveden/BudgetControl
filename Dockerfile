FROM python:3.12.0

COPY requirements.txt /app/
COPY main /app/main
COPY run.sh /app/

WORKDIR /app

RUN pip install -r requirements.txt

# Change working directory to /app/main
WORKDIR /app/main

RUN python creating_db_and_directories.py && rm creating_db_and_directories.py && rm create_db.sql

# Change back to /app
WORKDIR /app

CMD ["sh", "./run.sh"]

EXPOSE 5000
