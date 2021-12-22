FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4221200/snippet.py /snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
