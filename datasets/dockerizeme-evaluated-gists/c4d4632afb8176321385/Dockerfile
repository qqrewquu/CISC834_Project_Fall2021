FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c4d4632afb8176321385/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
