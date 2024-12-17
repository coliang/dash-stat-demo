FROM colin/flask-image

WORKDIR /app
COPY . /app/
ENV VIRTUAL_ENV=/app/.venv
ENV LOCAL_PYTHON=${VIRTUAL_ENV}/bin/python3

#RUN apt update
#RUN apt install make -y
RUN python3 -m venv ${VIRTUAL_ENV}
#RUN apt install npm -y
#RUN ${LOCAL_PYTHON} -m pip install --upgrade pip setuptools wheel
#RUN ${LOCAL_PYTHON} -m pip install -r requirements.txt
#RUN npm i -g less


CMD ["/app/.venv/bin/python3", "-m","main"]