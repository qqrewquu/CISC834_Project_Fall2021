FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7213533/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","Fabric3"]
RUN ["pip","install","boto"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
