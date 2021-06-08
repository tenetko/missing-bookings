# Build React application:

FROM node:alpine AS frontend_builder
WORKDIR /app/frontend

COPY ./frontend ./

RUN yarn
RUN yarn build


# Make a production image

FROM python:3.9-slim
WORKDIR /usr/src/app

COPY ./backend/Pipfile* ./
COPY ./backend/ .
COPY --from=frontend_builder app/frontend/build ./static

RUN pip install --upgrade pip \
&& pip install pipenv \
&& apt-get update \
&& apt-get autoremove -y \
&& apt-get clean \
&& pipenv install \
&& pipenv run tests

EXPOSE 80
CMD ["pipenv", "run", "server"]