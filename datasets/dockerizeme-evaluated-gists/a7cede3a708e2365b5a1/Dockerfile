FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a7cede3a708e2365b5a1/snippet.py /snippet.py
RUN ["pip","install","falcon"]
RUN ["pip","install","gevent"]
RUN ["pip","install","gevent-queue"]
CMD ["python","/snippet.py"]
