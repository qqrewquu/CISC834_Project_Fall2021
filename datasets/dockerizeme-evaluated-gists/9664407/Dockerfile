FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/9664407/snippet.py /snippet.py
RUN ["pip","install","redispy"]
RUN ["pip","install","redis"]
CMD ["python","/snippet.py"]
