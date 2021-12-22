FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3ec7f0791145b008589c/snippet.py /snippet.py
RUN ["pip","install","rethinkdb"]
CMD ["python","/snippet.py"]
