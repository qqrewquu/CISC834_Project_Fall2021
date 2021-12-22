FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/07c5bed2c94270c959c56c403396476d/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
