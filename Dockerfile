FROM alpine:latest


RUN apk add python3 git texlive-full vim
#RUN apt-get -y update

#RUN apt-get install -y python3

#RUN apk add --update py2-pip

#ADD requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/work/sources

CMD ["git","clone","https://github.com/laurentcarrie/jubilant-memory.git"]
WORKDIR /usr/src/work/sources/jubilant-memory
CMD ["git","checkout","moderncv-style"]
CMD ["git","pull"]
CMD ["ls","/usr/src/work/sources/jubilant-memory/py"]
WORKDIR /usr/src/work/sources/jubilant-memory/sources
CMD ["python3", "/usr/src/work/sources/jubilant-memory/py/all.py"]
