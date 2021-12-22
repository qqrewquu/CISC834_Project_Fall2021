FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4032651/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","17MonIP"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Twisted"]
RUN ["pip","install","IPy"]
RUN ["pip","install","ipython"]
RUN ["pip","install","Unum"]
CMD ["python","/snippet.py"]
