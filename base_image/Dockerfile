FROM python:3.11.0

WORKDIR /app
COPY . /app/
ENV VIRTUAL_ENV=/app/.venv
ENV LOCAL_PYTHON=${VIRTUAL_ENV}/bin/python3
RUN apt update
RUN python3 -m venv ${VIRTUAL_ENV}
RUN apt install npm -y
RUN ${LOCAL_PYTHON} -m pip install --upgrade pip setuptools wheel
RUN ${LOCAL_PYTHON} -m pip install -r requirements.txt
RUN npm i -g less