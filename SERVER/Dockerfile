FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"
ENV LIBRARY_PATH=/lib:/usr/lib

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers jpeg-dev libjpeg-turbo
RUN apk add build-base python3-dev zlib-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
RUN apk add libjpeg
RUN apk del .tmp

RUN mkdir /webserver
COPY ./webserver /webserver
WORKDIR /webserver
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]