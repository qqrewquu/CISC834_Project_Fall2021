FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/074587354d97d872aff6abb65510f618/snippet.py /snippet.py
RUN ["pip","install","numpy"]
RUN ["pip","install","joblib"]
RUN ["pip","install","s3io"]
CMD ["python","/snippet.py"]
