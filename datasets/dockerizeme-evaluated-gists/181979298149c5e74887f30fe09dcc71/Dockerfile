FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/181979298149c5e74887f30fe09dcc71/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
