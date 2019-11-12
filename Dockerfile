FROM python:3.7.4

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh

COPY ./app.py /app/app.py
COPY ./manage.py /app/manage.py
COPY ./config.json /app/config.json
COPY ./conf.py /app/conf.py
COPY ./models.py /app/models.py

ENTRYPOINT ["sh"]
CMD ["entrypoint.sh"]
