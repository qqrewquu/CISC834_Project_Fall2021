FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2c451bc515c6b8740b59/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
