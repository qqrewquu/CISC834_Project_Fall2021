FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/10796230/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
