FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/03aa9be710a5c93f6809f55dd0303e12/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","requests"]
RUN ["pip","install","colorama"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto3"]
CMD ["python","/snippet.py"]
