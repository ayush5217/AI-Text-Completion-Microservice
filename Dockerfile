# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install ctransformers-0.2.27-py3-none-any.whl
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]