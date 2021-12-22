FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/4da02e2960636d349e9bae7ae43c213c/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
