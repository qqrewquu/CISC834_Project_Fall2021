FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/10405384/snippet.py /snippet.py
RUN ["pip","install","locust"]
CMD ["python","/snippet.py"]
