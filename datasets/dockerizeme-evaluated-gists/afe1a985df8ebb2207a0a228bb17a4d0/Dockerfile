FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/afe1a985df8ebb2207a0a228bb17a4d0/snippet.py /snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
CMD ["python","/snippet.py"]
