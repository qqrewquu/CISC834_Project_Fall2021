FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5993501/snippet.py /snippet.py
RUN ["pip","install","Fabric3"]
RUN ["pip","install","envassert"]
RUN ["pip","install","fabric"]
CMD ["python","/snippet.py"]
