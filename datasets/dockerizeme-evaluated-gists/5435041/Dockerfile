FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5435041/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","pytest"]
RUN ["pip","install","py"]
RUN ["pip","install","PyTumblr"]
CMD ["python","/snippet.py"]
