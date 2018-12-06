FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /docker
 WORKDIR /docker
 ADD requirements.txt /docker/
 RUN pip install -r requirements.txt
 ADD . /docker/