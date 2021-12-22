FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8d931c29cf4562851ece7e39b7ec3b3d/snippet.py /snippet.py
RUN ["pip","install","jenkins-webapi"]
RUN ["pip","install","jenkins"]
CMD ["python","/snippet.py"]
