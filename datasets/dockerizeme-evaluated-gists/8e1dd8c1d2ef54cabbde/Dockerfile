FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8e1dd8c1d2ef54cabbde/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
