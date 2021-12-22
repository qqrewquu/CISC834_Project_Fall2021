FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9104225ab20c5c7b8d51190e56d9fff8/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
