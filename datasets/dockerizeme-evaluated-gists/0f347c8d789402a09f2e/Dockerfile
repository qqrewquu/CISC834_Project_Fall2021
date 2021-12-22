FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/0f347c8d789402a09f2e/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
