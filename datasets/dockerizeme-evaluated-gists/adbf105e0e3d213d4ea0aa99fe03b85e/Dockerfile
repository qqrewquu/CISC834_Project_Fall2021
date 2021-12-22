FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/adbf105e0e3d213d4ea0aa99fe03b85e/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
