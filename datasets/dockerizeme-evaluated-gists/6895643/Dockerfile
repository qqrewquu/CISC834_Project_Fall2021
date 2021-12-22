FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/6895643/snippet.py /snippet.py
RUN ["pip","install","networkx"]
RUN ["pip","install","numpy"]
CMD ["python","/snippet.py"]
