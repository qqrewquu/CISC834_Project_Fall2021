FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9996997/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","WebCore"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","git"]
RUN ["pip","install","six"]
RUN ["pip","install","PyYAML"]
RUN ["pip","install","docopt"]
RUN ["apt-get","install","-y","curl"]
RUN ["apt-get","install","-y","libssl-dev"]
RUN ["apt-get","install","-y","zlib1g-dev"]
RUN ["apt-get","install","-y","gcc"]
RUN ["apt-get","install","-y","ca-certificates"]
RUN ["apt-get","install","-y","make"]
RUN ["pip","install","docker-py"]
RUN ["apt-get","install","-y","zlib1g"]
RUN ["pip","install","dockerpty"]
RUN ["pip","install","texttable"]
RUN ["pip","install","websocket-client"]
RUN ["pip","install","websocket"]
CMD ["python","/snippet.py"]
