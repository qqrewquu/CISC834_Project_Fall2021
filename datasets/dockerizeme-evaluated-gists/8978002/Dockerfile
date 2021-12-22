FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/8978002/snippet.py /snippet.py
RUN ["pip","install","webvirtmgr"]
RUN ["pip","install","feedparser"]
RUN ["pip","install","console"]
CMD ["python","/snippet.py"]
