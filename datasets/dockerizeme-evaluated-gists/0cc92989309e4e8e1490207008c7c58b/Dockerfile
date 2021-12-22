FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0cc92989309e4e8e1490207008c7c58b/snippet.py /snippet.py
RUN ["pip","install","lxml"]
CMD ["python","/snippet.py"]
