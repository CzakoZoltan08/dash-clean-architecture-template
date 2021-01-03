FROM python:3.8

WORKDIR /code

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ./ ./

ENV ENVIRONMENT_FILE=".env"

EXPOSE 8085

#CMD ["python", "./index.py"]

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "index:server"]