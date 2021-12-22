FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/7cf9973676fe3e0bda30/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
RUN ["pip","install","scipy"]
CMD ["python","/snippet.py"]
