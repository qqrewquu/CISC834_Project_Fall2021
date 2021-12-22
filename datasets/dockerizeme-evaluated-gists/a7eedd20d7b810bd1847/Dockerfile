FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/a7eedd20d7b810bd1847/snippet.py /snippet.py
RUN ["pip","install","virtualenv"]
RUN ["pip","install","virtualenv-rewrite"]
CMD ["python","/snippet.py"]
