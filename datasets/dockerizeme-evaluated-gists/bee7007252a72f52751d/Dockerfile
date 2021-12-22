FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bee7007252a72f52751d/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
