FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a94ead037249f497a110763beb08942b/snippet.py /snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
CMD ["python","/snippet.py"]
