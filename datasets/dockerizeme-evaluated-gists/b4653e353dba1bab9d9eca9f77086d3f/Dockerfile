FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b4653e353dba1bab9d9eca9f77086d3f/snippet.py /snippet.py
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","libssl-dev"]
RUN ["pip","install","web3"]
RUN ["pip","install","marrow.mailer"]
RUN ["pip","install","marrow.schema"]
RUN ["pip","install","marrow.mongo"]
RUN ["pip","install","WebCore"]
CMD ["python","/snippet.py"]
