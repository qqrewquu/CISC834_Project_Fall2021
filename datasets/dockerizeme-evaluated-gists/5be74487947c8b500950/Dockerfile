FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5be74487947c8b500950/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","supervisor"]
RUN ["pip","install","supervisor-stdout"]
RUN ["pip","install","mock"]
RUN ["pip","install","pytest"]
RUN ["pip","install","ipdb"]
RUN ["apt-get","install","-y","exim4"]
RUN ["pip","install","graphite_beacon"]
RUN ["pip","install","funcparserlib"]
CMD ["python","/snippet.py"]
