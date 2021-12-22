FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6064607/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","suds"]
CMD ["python","/snippet.py"]
