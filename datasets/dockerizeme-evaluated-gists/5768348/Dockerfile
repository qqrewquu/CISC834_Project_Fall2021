FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5768348/snippet.py /snippet.py
RUN ["pip","install","bson"]
RUN ["pip","install","pymongo"]
CMD ["python","/snippet.py"]
