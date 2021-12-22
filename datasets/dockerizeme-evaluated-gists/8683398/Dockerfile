FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8683398/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","gevent"]
RUN ["pip","install","gevent-queue"]
CMD ["python","/snippet.py"]
