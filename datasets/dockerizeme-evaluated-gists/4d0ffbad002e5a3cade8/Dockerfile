FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4d0ffbad002e5a3cade8/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","youtube-python"]
RUN ["pip","install","pip"]
RUN ["pip","install","youtube_dl"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
