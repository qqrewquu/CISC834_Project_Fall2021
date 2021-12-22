FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5181480/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","WebCore"]
RUN ["apt-get","install","-y","python-pip"]
RUN ["apt-get","install","-y","python-dev"]
RUN ["pip","install","six"]
RUN ["pip","install","WebOb"]
CMD ["python","/snippet.py"]
