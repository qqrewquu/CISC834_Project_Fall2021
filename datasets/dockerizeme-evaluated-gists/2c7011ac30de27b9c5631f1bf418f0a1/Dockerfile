FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/2c7011ac30de27b9c5631f1bf418f0a1/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","matplotlib"]
CMD ["python","/snippet.py"]
