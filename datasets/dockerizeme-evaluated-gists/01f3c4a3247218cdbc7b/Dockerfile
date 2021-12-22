FROM python:2.7.13
COPY ../datasets/dockerizeme-evaluated-gists/01f3c4a3247218cdbc7b/snippet.py /snippet.py
RUN ["pip","install","rdflib"]
CMD ["python","/snippet.py"]
