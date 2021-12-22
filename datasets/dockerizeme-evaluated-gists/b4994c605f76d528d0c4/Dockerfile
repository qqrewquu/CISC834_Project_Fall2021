FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b4994c605f76d528d0c4/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
