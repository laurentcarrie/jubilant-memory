FROM alpine:latest


RUN apk add python3 git texlive
#RUN apt-get -y update

#RUN apt-get install -y python3

#RUN apk add --update py2-pip

ADD requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

ADD sources /usr/src/app/sources

VOLUME /usr/src/app/sources
WORKDIR /usr/src/app/sources
#CMD ["python", "/usr/src/app/sources/go.py"]

RUN ls -R /usr/src/app/sources

