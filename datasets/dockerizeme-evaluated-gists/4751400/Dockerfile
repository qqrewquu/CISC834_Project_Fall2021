FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4751400/snippet.py /snippet.py
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
