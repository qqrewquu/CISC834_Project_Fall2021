FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/ba7b46dfc854544bf3c8/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","Jinja2"]
RUN ["pip","install","boto"]
RUN ["pip","install","xmltodict"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
