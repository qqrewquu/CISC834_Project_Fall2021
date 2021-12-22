FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5799103/snippet.py /snippet.py
RUN ["pip","install","celery"]
CMD ["python","/snippet.py"]
