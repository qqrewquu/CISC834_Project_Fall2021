FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4151154/snippet.py /snippet.py
RUN ["pip","install","green"]
RUN ["pip","install","six"]
RUN ["pip","install","greenlet"]
CMD ["python","/snippet.py"]
