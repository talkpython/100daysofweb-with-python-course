FROM base_server:latest

RUN apt-get install -y -q build-essential git python3-pip python3-dev python3-venv
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip setuptools
RUN /venv/bin/pip install responder

COPY movie_svc /app
WORKDIR /app
RUN /venv/bin/pip install -r /app/requirements.txt

ENTRYPOINT /venv/bin/python /app/app.py
