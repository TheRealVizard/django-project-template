FROM python:3.10.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

WORKDIR /code

RUN apt-get install -y gcc libpq-dev

# Install requirements
RUN pip install --upgrade pip
RUN pip install poetry

ADD poetry.lock /code/
ADD pyproject.toml /code/
RUN poetry config virtualenvs.create false

RUN /bin/sh -c 'poetry install --no-dev --no-interaction --no-root'

COPY . /code/

RUN mkdir -p /code/{{ project_name }}/staticfiles

EXPOSE 8000
