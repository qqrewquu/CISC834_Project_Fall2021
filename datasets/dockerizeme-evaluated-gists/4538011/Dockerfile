FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4538011/snippet.py /snippet.py
RUN ["pip","install","mock"]
RUN ["pip","install","pyte"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
