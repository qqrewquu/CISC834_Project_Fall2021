FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6df33e9cafa4d84005bf/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
