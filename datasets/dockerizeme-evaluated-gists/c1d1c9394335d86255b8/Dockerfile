FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/c1d1c9394335d86255b8/snippet.py /snippet.py
RUN ["pip","install","six"]
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
