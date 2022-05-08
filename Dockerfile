FROM python:3.10-slim as development

WORKDIR /usr/src/app
COPY ./pyproject.toml /usr/src/app/
COPY ./poetry.lock /usr/src/app/

RUN pip3 install poetry
RUN poetry install

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG_MODE=true
# secrets
ENV INTERNAL_API_KEY=${INTERNAL_API_KEY}
ENV DEBUG_SECRET=${DEBUG_SECRET}
ENV DEBUG_USER_PASSWORD=${DEBUG_USER_PASSWORD}
ENV SECRET=${SECRET}
ENV JWT_ACCESS_SECRET=${JWT_ACCESS_SECRET}
ENV JWT_REFRESH_SECRET=${JWT_REFRESH_SECRET}
# other vars
ENV DATABASE_URL=${DATABASE_URL}
ENV DATABASE_NAME=${DATABASE_NAME}

COPY . /usr/src/app/

ENTRYPOINT ["/bin/sh", "start.sh"]

##########################
#    PRODUCTION CONF     #
##########################

FROM python:3.10-slim as production

WORKDIR /usr/src/app/
COPY ./pyproject.toml /usr/src/app/
COPY ./poetry.lock /usr/src/app/

RUN pip3 install poetry
RUN poetry install

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG_MODE=false
# secrets
ENV INTERNAL_API_KEY=${INTERNAL_API_KEY}
ENV DEBUG_SECRET=${DEBUG_SECRET}
ENV DEBUG_USER_PASSWORD=${DEBUG_USER_PASSWORD}
ENV SECRET=${SECRET}
ENV JWT_ACCESS_SECRET=${JWT_ACCESS_SECRET}
ENV JWT_REFRESH_SECRET=${JWT_REFRESH_SECRET}
# other vars
ENV DATABASE_URL=${DATABASE_URL}
ENV DATABASE_NAME=${DATABASE_NAME}

COPY . /usr/src/app/

ENTRYPOINT ["/bin/sh", "start.sh"]
