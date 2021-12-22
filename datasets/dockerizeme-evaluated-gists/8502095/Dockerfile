FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8502095/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","fabric"]
RUN ["pip","install","fabric-utils"]
CMD ["python","/snippet.py"]
