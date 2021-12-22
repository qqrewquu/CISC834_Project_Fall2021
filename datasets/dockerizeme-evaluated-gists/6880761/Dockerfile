FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6880761/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
