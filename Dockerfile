# Build React application:

FROM node:alpine AS frontend_builder
WORKDIR /app/frontend

COPY ./frontend ./

RUN yarn
RUN yarn build


# Make a production image

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /usr/src/app

COPY ./backend/Pipfile* ./
COPY ./backend/ .
COPY --from=frontend_builder app/frontend/build ./static

RUN pip install --upgrade pip \
&& pip install pipenv \
&& pipenv install \
&& pipenv run tests

EXPOSE 80
CMD ["sh", "-c", "~/.venv/bin/uvicorn main:app --host=0.0.0.0 --port=$PORT"]