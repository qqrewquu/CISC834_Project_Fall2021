FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6877402a5705c84dd2ac/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
