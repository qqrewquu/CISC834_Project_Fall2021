FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/bb73f21ed2f3b46bc1c2ca48ec2c1cf5/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
