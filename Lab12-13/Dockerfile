FROM python:2.7

RUN apt-get update
RUN apt-get -y upgrade

RUN pip install flask boto

ADD /boto-rest.py /boto-rest.py

CMD python /boto-rest.py

EXPOSE 5000
