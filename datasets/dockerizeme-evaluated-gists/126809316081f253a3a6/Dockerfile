FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/126809316081f253a3a6/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Twisted"]
RUN ["pip","install","IPy"]
RUN ["pip","install","17MonIP"]
RUN ["pip","install","networkx"]
RUN ["pip","install","ipython"]
CMD ["python","/snippet.py"]
