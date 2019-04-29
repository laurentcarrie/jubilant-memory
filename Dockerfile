FROM alpine:latest


RUN apk add python3 git texlive-full
#RUN apt-get -y update

#RUN apt-get install -y python3

#RUN apk add --update py2-pip

#ADD requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/work/sources

RUN git clone https://github.com/laurentcarrie/jubilant-memory.git

#CMD ["python3", "build_cv.py"]
