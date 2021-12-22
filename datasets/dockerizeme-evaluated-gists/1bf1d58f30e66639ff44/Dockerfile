FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1bf1d58f30e66639ff44/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","pyte"]
CMD ["python","/snippet.py"]
