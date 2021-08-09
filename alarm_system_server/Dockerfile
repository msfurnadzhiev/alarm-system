FROM python:3.8-alpine3.13

RUN mkdir -p /app/install
WORKDIR /app
COPY install/requirements.txt /app/install
RUN pip install -r install/requirements.txt

COPY src /app/src
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]