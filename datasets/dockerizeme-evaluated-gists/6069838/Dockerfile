FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6069838/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","dnspython"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["pip","install","dnslib"]
CMD ["python","/snippet.py"]
