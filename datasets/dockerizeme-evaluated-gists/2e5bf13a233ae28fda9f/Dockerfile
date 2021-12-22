FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2e5bf13a233ae28fda9f/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
