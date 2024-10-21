FROM python:3.11.0

WORKDIR /app
COPY . /app/
RUN apt update
RUN apt install make -y
RUN apt install npm -y

CMD ["make", "deploy"]