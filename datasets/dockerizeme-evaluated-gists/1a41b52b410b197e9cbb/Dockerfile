FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/1a41b52b410b197e9cbb/snippet.py /snippet.py
RUN ["pip","install","scraperwiki"]
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
