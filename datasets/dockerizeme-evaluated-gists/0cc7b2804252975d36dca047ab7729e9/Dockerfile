FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0cc7b2804252975d36dca047ab7729e9/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
