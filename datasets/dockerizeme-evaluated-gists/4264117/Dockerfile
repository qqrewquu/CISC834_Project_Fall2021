FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4264117/snippet.py /snippet.py
RUN ["pip","install","boto-mws"]
RUN ["pip","install","boto"]
RUN ["pip","install","boto-patch"]
CMD ["python","/snippet.py"]
