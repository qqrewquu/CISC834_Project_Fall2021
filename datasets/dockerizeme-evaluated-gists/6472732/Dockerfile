FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6472732/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dnspython"]
RUN ["pip","install","requests"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","dnslib"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
