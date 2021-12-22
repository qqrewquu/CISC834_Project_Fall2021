FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/b9c5b5529381d1737fc3/snippet.py /snippet.py
RUN ["pip","install","requests"]
RUN ["pip","install","ntfy"]
CMD ["python","/snippet.py"]
