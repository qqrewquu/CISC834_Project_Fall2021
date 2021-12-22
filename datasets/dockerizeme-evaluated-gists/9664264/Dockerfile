FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9664264/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto"]
CMD ["python","/snippet.py"]
