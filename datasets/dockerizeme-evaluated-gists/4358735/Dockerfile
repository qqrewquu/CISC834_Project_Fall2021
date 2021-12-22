FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4358735/snippet.py /snippet.py
RUN ["pip","install","bottle"]
RUN ["pip","install","gevent"]
CMD ["python","/snippet.py"]
