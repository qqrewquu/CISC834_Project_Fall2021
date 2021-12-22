FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c1feef2bf7a3a014178c/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","celery"]
CMD ["python","/snippet.py"]
