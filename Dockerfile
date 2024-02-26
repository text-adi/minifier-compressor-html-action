FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt


FROM python:3.12-slim

LABEL "com.github.actions.name"="Minify html files"
LABEL "com.github.actions.description"="Minify html using the minify html library"
LABEL "com.github.actions.icon"="refresh-ccw"
LABEL "com.github.actions.color"="green"

LABEL version="2"
LABEL repository="https://github.com/text-adi/minifier-compressor-html-action"
LABEL homepage="https://github.com/text-adi"
LABEL maintainer="text-adi <text-adi@github.com>"

WORKDIR /code

COPY --chmod=700 script /script

COPY --from=builder /install /usr/local/

CMD ["python","/script/main.py"]