FROM python:3.8-slim

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

RUN apt-get autoremove -y --purge && \
    apt-get clean -y

WORKDIR /app
CMD python manage.py runserver 0.0.0.0:8000