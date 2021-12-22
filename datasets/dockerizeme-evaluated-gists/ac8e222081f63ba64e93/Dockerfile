FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ac8e222081f63ba64e93/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
RUN ["pip","install","python-dateutil"]
RUN ["pip","install","six"]
RUN ["pip","install","requests"]
RUN ["pip","install","botocore"]
CMD ["python","/snippet.py"]
