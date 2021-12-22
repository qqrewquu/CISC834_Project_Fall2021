FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/00c8d9dfc21591a0de16dad7a8737c3b/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","17MonIP"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["apt-get","install","-y","build-essential"]
RUN ["pip","install","Twisted"]
RUN ["pip","install","IPy"]
RUN ["pip","install","ipython"]
CMD ["python","/snippet.py"]
