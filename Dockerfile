#FROM python:3.6
#ADD . /app
#WORKDIR /app
#RUN pip install -r requirments.txt

FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install flask flask-pymongo flask-wtf
COPY . /app
WORKDIR /app
