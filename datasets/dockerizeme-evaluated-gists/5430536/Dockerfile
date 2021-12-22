FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5430536/snippet.py /snippet.py
RUN ["pip","install","PyTumblr"]
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
CMD ["python","/snippet.py"]
