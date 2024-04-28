#
#FROM python:3.9
FROM python:3.11.1-slim
#
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
COPY requirements.txt /code/requirements.txt

#
RUN pip install -r /code/requirements.txt

#
COPY ./todo /code/todo

#
#CMD ["uvicorn", "todo.app:app", "--host", "0.0.0.0", "--port", "80"]