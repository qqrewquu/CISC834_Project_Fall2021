FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/3481728/snippet.py /snippet.py
RUN ["pip","install","feedparser"]
CMD ["python","/snippet.py"]
