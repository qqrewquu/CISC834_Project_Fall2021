FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5cd4dceb9e4f40d110ef/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","requests"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
