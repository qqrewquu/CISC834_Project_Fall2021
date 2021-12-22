FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/03e309b89fd9a74af1dd41344b7c5c70/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
