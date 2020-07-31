FROM python:alpine3.7
ENV PYTHONUNBUFFERED 1
RUN \
 apk add --no-cache libffi-dev && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN mkdir /todo
WORKDIR /todo
COPY . /todo
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
ENTRYPOINT ["sh","script/entrypoint.sh"] 