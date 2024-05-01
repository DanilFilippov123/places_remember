FROM python:3.10-alpine3.19

RUN apk update && \
    apk add --virtual build-deps gcc && \
    apk add postgresql-dev

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["sh", "/usr/src/app/docker/start.sh"]