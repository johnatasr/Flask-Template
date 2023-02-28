FROM python:3.10

WORKDIR /usr/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV PYTHONPATH /usr/app

COPY /pyproject.toml /usr/app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.path /usr/app/

RUN poetry install

COPY . .

EXPOSE 5000

#Dev
# CMD ["python", "manage.py", "runserver"]
