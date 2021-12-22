FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/5671071/snippet.py /snippet.py
RUN ["pip","install","Flask"]
RUN ["pip","install","neo4j-driver"]
RUN ["pip","install","neo4jrestclient"]
CMD ["python","/snippet.py"]
