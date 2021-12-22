FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6b572512ef53cfc6bf949afdc8eb6720/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
