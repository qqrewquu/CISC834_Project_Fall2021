FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4a5fe88be8923bea19c02e5641be33b2/snippet.py /snippet.py
RUN ["pip","install","boto-patch"]
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
CMD ["python","/snippet.py"]
