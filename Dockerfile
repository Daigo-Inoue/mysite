FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /mysite
COPY requirements.txt /mysite/
RUN pip install -r requirements.txt
COPY . /mysite/